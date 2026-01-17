# 🪙 BTC AI Terminal: Deep Learning & Telegram Automation 🤖

[![Live App](https://img.shields.io/badge/Streamlit-Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit)](https://sofien-btc-ai-terminal.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)](https://www.tensorflow.org/)

---

## 📖 Project Vision
**BTC AI Terminal** is an end-to-end financial ecosystem designed to bridge the gap between **Deep Learning** and **Real-time Trading**. This project doesn't just display data; it uses a trained **LSTM (Long Short-Term Memory)** neural network to predict Bitcoin price movements and automates the delivery of these insights directly to your pocket via Telegram.

---

## 🚀 Live Deployment
The application is hosted on **Streamlit Cloud** and runs 24/7.
🔗 **Access the Terminal:** [https://sofien-btc-ai-terminal.streamlit.app/](https://sofien-btc-ai-terminal.streamlit.app/)

---

## 🛠️ Core Features

### 1. **AI-Powered Forecasting**
- Uses an **LSTM Neural Network**, specifically chosen for its ability to remember long-term dependencies in time-series data (like crypto prices).
- Processes historical data (Open, High, Low, Close, Volume) to predict the next market trend.

### 2. **Interactive Dashboard**
- Real-time Bitcoin charts using **Plotly**.
- Technical indicators (Moving Averages, RSI).
- A "Manual Analysis" trigger to get AI predictions on demand.

### 3. **Telegram Automation**
- An integrated **Scheduler** that runs in the background.
- Automatically fetches data, runs the AI model, and sends a "Buy/Sell/Hold" signal to a specific Telegram Chat ID every 4 hours.

---

## 🏗️ Technical Architecture

### **The Stack**
- **Frontend:** Streamlit (Python-based Web Framework).
- **Backend Engine:** TensorFlow & Keras (for the AI model).
- **Data Source:** Yahoo Finance API (`yfinance`).
- **Automation:** `schedule` library for periodic tasks.
- **Data Processing:** Pandas, NumPy, and Scikit-Learn.

### **Project Directory**
```text
📂 BTC_AI_Terminal
├── app.py                 # The heart of the web interface
├── btc_model.h5           # The brain (Trained LSTM Model)
├── my_scaler.pkl          # Data normalizer (MinMaxScaler)
├── requirements.txt       # List of all Python dependencies
├── .gitignore             # Security: hides config.py and venv
├── utils/
│   ├── ai_engine.py       # Logic for data fetching and AI inference
│   └── automation.py      # Logic for Telegram Bot and Scheduling
└── notebooks/             # Research & Training phase files

```
## 💻 Installation & Setup

If you want to run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/BTC_AI_Terminal.git](https://github.com/YOUR_USERNAME/BTC_AI_Terminal.git)
cd BTC_AI_Terminal
```
###  Create the environment
```bash
python -m venv venv
```
###  Activate it (Windows)
```bash
.\venv\Scripts\activate
```
###  Activate it (Mac/Linux)
```bash
source venv/bin/activate
```
### Install Requirement
```bash
pip install -r requirements.txt
```
### . Setup Telegram Credentials (IMPORTANT)
To get your signals, you need to:
1. Message **@BotFather** on Telegram to create a bot and get your `TOKEN`.
2. Message **@userinfobot** to get your `CHAT_ID`.
3. Create a `config.py` file in the root folder:


###  Telegram config
```bash
python
TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"
```

### Run the Terminal
```bash
streamlit run app.py
```
---

## 👤 Author
**Project Created by Sofien | Data Science Enthusiast**

If you want to see more of my work and explore my professional background:
🚀 **Visit my Portfolio:** [Sofien Meftahi Studio | Data Analyst & BI Developer](https://sofien-meftahi-studio.framer.website/)

---
*Stay connected and feel free to reach out for collaborations!*
