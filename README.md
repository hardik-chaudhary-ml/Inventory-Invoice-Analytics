# 🚀 Vendor Invoice Intelligence System

An end-to-end Machine Learning project to predict freight cost and detect risky invoices, helping automate financial decision-making and reduce manual approval workload.

---

## 🎯 Project Objective

This system is designed to:

- 📦 Predict Freight Cost (Regression)
- 🚨 Detect Risky Invoices (Classification)
- 💼 Reduce manual approval workload
- 💰 Improve financial decision-making

---

## 🧠 Project Overview

This project assists finance teams by:

- Predicting freight cost for invoices  
- Detecting high-risk invoices requiring manual approval  
- Reducing financial leakage and operational effort  

---

## ⭐ Key Features

- End-to-end ML pipeline (data → model → deployment)  
- Feature engineering using SQL aggregation  
- Model comparison (Linear, Decision Tree, Random Forest)  
- Hyperparameter tuning using GridSearchCV  
- Real-time prediction using Streamlit UI  

---

## 📊 Exploratory Data Analysis (EDA)

Key insights from data:

- Most invoices fall in a mid-range value distribution  
- Freight cost increases with invoice amount  
- Some invoices show abnormal patterns indicating risk  



---

## 🤖 Models Used

### Regression (Freight Cost)
- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor (Final Model)  

### Classification (Invoice Flagging)
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier (Final Model)  

---

## 📈 Model Performance

### Regression
- MAE: 12.5  
- RMSE: 18.2  
- R² Score: 0.82  

### Classification
- Accuracy: 89%  
- Precision: 0.87  
- Recall: 0.85  
- F1-score: 0.86  

---

## 💡 Business Insights

- High difference between Invoice Amount and Item Value indicates potential fraud  
- Unusually high freight cost is a strong anomaly signal  
- Automation reduces manual effort and speeds up approvals  

---

---

## 📂 Data Source

* Data stored in SQLite database (`inventory.db`)
* Includes invoice-level and item-level transaction data
* Features engineered using SQL aggregation

---

## 📂 Dataset

Due to GitHub file size limits, the dataset is not stored in this repository.

Instead, it is hosted on Google Drive.

### 🔽 Download Dataset

Run:

```bash
python download_db.py

```
## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---
```
## 📁 Project Structure

```
Inventory-Invoice-Analytics/

├── data/
│   └── inventory.db

├── freight_cost_prediction/
│   ├── data_preprocessing.py
│   ├── modeling_evaluation.py
│   ├── train.py

├── invoice_flagging/
│   ├── data_preprocessing.py
│   ├── modeling_evaluation.py
│   ├── train.py

├── inference/
│   ├── predict_freight.py
│   ├── predict_invoice_flag.py

├── models/
│   ├── predict_freight_model.pkl
│   ├── predict_flag_invoice.pkl
│   ├── scaler.pkl

├── images/
│   ├── freight_normal.png
│   ├── freight_low.png
│   ├── invoice_safe.png
│   ├── invoice_manual.png

├── app.py
├── requirements.txt
└── README.md
----download_db.py

```

---

## 📸 Output Screens

Output are stored in images folder

## 🧠 Decision Logic

The prediction is based on:

* 📊 Difference between *Invoice Dollars* and *Total Item Dollars*
* 🚚 Freight cost relative to invoice amount
* ⏱ Delivery delay (receiving delay)

---

## ✅ Example (SAFE Case)

| Feature             | Value |
| ------------------- | ----- |
| Invoice Quantity    | 50    |
| Invoice Dollars     | 2500  |
| Total Item Dollars  | 2480  |
| Freight Cost        | 50    |
| Total Item Quantity | 160   |

👉 Output: **0 (SAFE for Auto Approval)**

---

## 🚨 Example (Manual Approval Case)

| Feature             | Value |
| ------------------- | ----- |
| Invoice Quantity    | 50    |
| Invoice Dollars     | 2500  |
| Total Item Dollars  | 1500  |
| Freight Cost        | 800   |
| Total Item Quantity | 160   |

👉 Output: **1 (Requires MANUAL APPROVAL)**

---

## 🤖 Models Used

### 📊 Regression (Freight Cost)

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor (**Final Model**)

### 🚨 Classification (Invoice Flagging)

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier (**Final Model**)

---

## 📈 Evaluation Metrics

### Regression

* MAE (Mean Absolute Error)
* RMSE
* R² Score

### Classification

* Accuracy
* Precision, Recall, F1-score
* Classification Report

---

## 🚀 Future Improvements

* Deploy on cloud (Streamlit Cloud / AWS)
* Add real-time database integration
* Improve model accuracy using advanced algorithms

---

## ⚙️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the App

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Hardik Chaudhary**
B.Tech CSE | Aspiring Data Analyst / Data Scientist

📧 Email: [hardik1chaudhary@gmail.com](mailto:hardik1chaudhary@gmail.com)
