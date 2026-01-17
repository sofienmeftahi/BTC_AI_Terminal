import requests
import schedule
import time
import threading
import streamlit as st

# Integrated Configuration Loader
# Checks Streamlit Cloud Secrets first, then falls back to local config.py
try:
    TOKEN = st.secrets["TOKEN"]
    CHAT_ID = st.secrets["CHAT_ID"]
except Exception:
    try:
        from config import TOKEN, CHAT_ID
    except ImportError:
        TOKEN = None
        CHAT_ID = None

def send_telegram_signal(signal, curr_p, pred_p, diff, emo, type_msg="MANUAL"):
    """
    Sends a professionally formatted trading signal to the Telegram Bot.
    Includes current price, AI target price, and percentage difference.
    """
    if not TOKEN or not CHAT_ID:
        print("System Error: Telegram credentials missing.")
        return

    # Message formatting using Markdown for better visual appeal on Telegram
    message = (
        f"{emo} *NEW AI SIGNAL ({type_msg})*\n\n"
        f"Asset: *BTC/USD*\n"
        f"Action: *{signal}*\n"
        f"Current Price: *${curr_p:,.2f}*\n"
        f"Target Price: *${pred_p:,.2f}*\n"
        f"Prediction Change: *{diff*100:.2f}%*\n\n"
        f"🤖 _Neural Inference Engine: Sofien's Terminal_"
    )
    
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        # Executing the request with parameters for safe URL handling
        response = requests.get(api_url, params=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Network Error: Unable to reach Telegram API. Details: {e}")

def start_scheduler(job_function):
    """
    Launches a background thread to handle automated tasks.
    The scheduler is configured to trigger every 4 hours.
    """
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(60) # Checks for pending tasks every minute
            
    # Interval configuration: 4-hour cycles
    schedule.every(4).hours.do(job_function)
    
    # Daemonizing the thread ensures it closes when the main app exits
    bg_thread = threading.Thread(target=run_scheduler, daemon=True)
    bg_thread.start()