import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components

# Import modular components
from assets.style import apply_custom_css, get_signal_card
from utils.ai_engine import load_ai_assets, get_prediction
from utils.automation import send_telegram_signal, start_scheduler

# --- 1. System Setup ---
st.set_page_config(page_title="QUANT AI", page_icon="📡", layout="wide")
apply_custom_css()

# --- 2. Background Automation ---
def daily_job():
    c_p, p_p, _ = get_prediction()
    if c_p and p_p:
        diff = (p_p - c_p) / c_p
        emo = "🚀" if diff > 0.005 else "🛑" if diff < -0.005 else "⏳"
        sig = "STRONG BUY" if diff > 0.005 else "SELL" if diff < -0.005 else "HOLD"
        send_telegram_signal(sig, c_p, p_p, diff, emo, type_msg="DAILY AUTO")

if 'scheduler_started' not in st.session_state:
    start_scheduler(daily_job)
    st.session_state['scheduler_started'] = True

# --- 3. Dashboard Header ---
st.markdown("<h1 class='main-header'>📡 AI QUANTUM TERMINAL: BTC/USD</h1>", unsafe_allow_html=True)

model, scaler = load_ai_assets()

if model and scaler:
    # Data Fetching
    df = yf.download("BTC-USD", period="200d", interval="1d", auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex): 
        df.columns = df.columns.get_level_values(0)

    curr_p = float(df['Close'].iloc[-1])
    change = float(((df['Close'].iloc[-1] - df['Close'].iloc[-2]) / df['Close'].iloc[-2]) * 100)

    # Sidebar
    st.sidebar.markdown("### 🛠️ CORE STATUS")
    st.sidebar.success("NEURAL ENGINE: ONLINE")

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("💎 LIVE PRICE", f"${curr_p:,.2f}", f"{change:.2f}%")
    m2.metric("📈 24H HIGH", f"${df['High'].iloc[-1]:,.0f}")
    m3.metric("📉 24H LOW", f"${df['Low'].iloc[-1]:,.0f}")
    m4.metric("📊 VOL (24H)", f"{df['Volume'].iloc[-1]:,.0f}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Grid
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📊 MARKET FLOW")
        tv_widget = '<div style="height:550px;"><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize": true, "symbol": "BINANCE:BTCUSDT", "interval": "D", "theme": "dark", "container_id": "tv_chart"});</script><div id="tv_chart" style="height:550px;"></div></div>'
        components.html(tv_widget, height=560)

    with col_right:
        st.subheader("🧠 AI INFERENCE")
        if st.button("🚀 EXECUTE NEURAL ANALYSIS"):
            with st.spinner('Thinking...'):
                c_p, p_p, _ = get_prediction()
                if c_p and p_p:
                    diff = (p_p - c_p) / c_p
                    # Logic for Colors
                    if diff > 0.005: 
                        sig, col, emo, glow = "STRONG BUY", "#00ffcc", "🚀", "rgba(0,255,204,0.15)"
                    elif diff < -0.005: 
                        sig, col, emo, glow = "SELL", "#ff4b4b", "🛑", "rgba(255, 75, 75, 0.15)"
                    else: 
                        sig, col, emo, glow = "HOLD", "#ffff00", "⏳", "rgba(255, 255, 0, 0.1)"
                    
                    # Display Signal from assets/style.py
                    st.markdown(get_signal_card(sig, col, emo, glow), unsafe_allow_html=True)
                    st.metric("TARGET PRICE", f"${p_p:,.2f}", f"{diff*100:.2f}%")
                    
                    # --- Send Signal & Show Status ---
                    send_telegram_signal(sig, c_p, p_p, diff, emo, type_msg="MANUAL")
                    
                    # الـ Message المزيانة اللي تظهر لوطة على اليمين وتختفي وحدها
                    st.toast(f'Signal Transmitted to Telegram Bot {emo}', icon='📡')

                    # Prediction Visual
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index[-25:], y=df['Close'][-25:], name='Price', line=dict(color='#00d4ff')))
                    fig.add_trace(go.Scatter(x=[df.index[-1], df.index[-1] + pd.Timedelta(days=1)], y=[curr_p, p_p], name='AI', line=dict(color=col, dash='dot')))
                    fig.update_layout(template="plotly_dark", height=250, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.error("System Error: Check AI model path.")