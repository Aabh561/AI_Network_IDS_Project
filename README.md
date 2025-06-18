# AI-Driven Network Intrusion Detection with Real-Time Deep Packet Analysis

## 🔍 Overview
This project builds an AI-based Network Intrusion Detection System using LSTM, real and synthetic traffic data, and real-time classification & visualization.

## 📂 Components
- `NetworkIDS_LSTM.ipynb`: LSTM model for classifying intrusions on NSL-KDD
- `network_generator.py`: Generates synthetic traffic with attack types
- `dashboard.ipynb`: Live traffic dashboard with Plotly
- `utils.py`: Helpers for parsing logs and feature scaling

## 📊 Datasets
- `NSL-KDD`: Used for model training/testing (`data/real/NSL_KDD`)
- `Synthetic`: Generated CSV logs (`data/synthetic/sample_log.csv`)

## ▶️ How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run `network_generator.py` to create synthetic data
3. Use `NetworkIDS_LSTM.ipynb` to train/test model
4. Visualize with `dashboard.ipynb`

## 🛡️ Attacks Detected
- Normal, DDoS, SQL Injection, Port Scan, Brute Force

## 📁 Folder Structure
- `data/real/NSL_KDD/`: Put `KDDTrain+.txt` and `KDDTest+.txt`
- `data/synthetic/`: Contains generated logs

## 📈 Libraries Used
TensorFlow, Scikit-learn, Pandas, Plotly, Ipywidgets, Scapy (optional for live capture)

---

Created with ❤️ for academic/research use.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Aabh561/AI_Network_IDS_Project/blob/main/NetworkIDS_LSTM.ipynb)

