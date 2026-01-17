import streamlit as st

def apply_custom_css():
    """Injects all CSS styles into the app."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;700&display=swap');
        
        .stApp {
            background: radial-gradient(circle at top right, #000814, #000000);
            color: #e0e0e0;
            font-family: 'Inter', sans-serif;
        }

        .main-header {
            font-family: 'Orbitron', sans-serif;
            color: #00d4ff !important;
            text-align: center;
            text-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
            letter-spacing: 5px;
            padding: 20px;
            border-bottom: 1px solid #111;
            margin-bottom: 30px;
        }

        div[data-testid="stMetric"] {
            background: rgba(0, 212, 255, 0.03);
            border: 1px solid rgba(0, 212, 255, 0.1);
            padding: 15px;
            border-radius: 12px;
            transition: 0.3s ease-in-out;
        }
        div[data-testid="stMetric"]:hover {
            border-color: #00d4ff;
            background: rgba(0, 212, 255, 0.07);
            transform: translateY(-3px);
        }

        .stButton>button {
            width: 100%;
            background: linear-gradient(45deg, #00d4ff, #0077ff);
            color: white !important;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            padding: 12px;
            font-family: 'Orbitron', sans-serif;
            box-shadow: 0 4px 15px rgba(0, 119, 255, 0.3);
            transition: 0.3s;
        }
        .stButton>button:hover {
            box-shadow: 0 0 25px rgba(0, 212, 255, 0.5);
            transform: scale(1.02);
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)

def get_signal_card(sig, col, emo, glow):
    """Returns a styled HTML card for the AI prediction result."""
    return f"""
        <div style="background:{glow}; border: 2px solid {col}; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 0 30px {col}44; margin-bottom: 20px;">
            <h1 style='color:{col} !important; margin:0; font-family:Orbitron; font-size: 35px; border:none; text-shadow: 0 0 10px {col};'>{emo} {sig}</h1>
            <p style='color:#aaa; font-size: 14px; margin-top:10px; letter-spacing:1px;'>AI CORE INFERENCE COMPLETE</p>
        </div>
    """