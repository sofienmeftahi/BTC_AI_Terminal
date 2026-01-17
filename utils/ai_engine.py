import os
import joblib
import numpy as np
import pandas as pd
import yfinance as yf
from tensorflow.keras.models import load_model
import streamlit as st

@st.cache_resource
def load_ai_assets():
    """Loads the H5 model and the saved Scaler from the local directory."""
    if os.path.exists('btc_model.h5') and os.path.exists('my_scaler.pkl'):
        # compile=False avoids version mismatch issues between Colab and PC
        model = load_model('btc_model.h5', compile=False)
        scaler = joblib.load('my_scaler.pkl')
        return model, scaler
    return None, None

def get_prediction():
    """Fetches market data and returns the current price and LSTM prediction."""
    df = yf.download("BTC-USD", period="200d", interval="1d", auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex): 
        df.columns = df.columns.get_level_values(0)
    
    model, scaler = load_ai_assets()
    if model is not None and scaler is not None:
        try:
            curr_price = float(df['Close'].iloc[-1])
            # Prepare the last 60 days of closing prices for prediction
            last_60_days = df['Close'].tail(60).values.reshape(-1, 1)
            scaled_input = scaler.transform(last_60_days)
            X_test = np.reshape(scaled_input, (1, 60, 1))

            predicted_scaled = model.predict(X_test, verbose=0)
            predicted_price = float(scaler.inverse_transform(predicted_scaled)[0][0])
            return curr_price, predicted_price, df
        except Exception as e:
            print(f"Prediction logic error: {e}")
            return None, None, None
    return None, None, None