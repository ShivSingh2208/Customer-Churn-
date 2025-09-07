## 📅 Project Timelinemer Churn Prediction & Retention Analysis

This project presents a complete pipeline to predict customer churn and derive actionable insights for improving customer retention in the telecom industry. It includes **data analysis**, **feature engineering**, **machine learning**, and a deployed **interactive Streamlit web app**.

## � Author
**Shiv Singh**
- GitHub: [@ShivSingh2208](https://github.com/ShivSingh2208)

## 📅 Project Timeline
- September 2025: Initial project setup and data analysis
- Added machine learning models and feature engineering
- Implemented Streamlit web interface for predictions

## �🚀 Project Overview

🔍 **Goal**: Identify customers likely to churn and uncover key behavioral patterns to improve retention.  
📊 **Tech Stack**: Python, Pandas, Scikit-learn, Streamlit, Matplotlib, Seaborn

---

## 📁 Dataset Description

The dataset simulates customer data for a telecom service provider and includes:

| Column           | Description |
|------------------|-------------|
| `CustomerID`     | Unique ID for each customer |
| `Age`            | Customer's age |
| `Gender`         | Male or Female |
| `Tenure`         | Number of months with the service |
| `MonthlyCharges` | Monthly service charges |
| `TotalCharges`   | Total amount charged to date |
| `ContractType`   | Contract type (Month-to-Month, One-Year, Two-Year) |
| `InternetService`| Type of internet service |
| `TechSupport`    | Whether tech support is subscribed |
| `Churn`          | Target variable (Yes/No) |

---

## 🔧 Features & Workflow

### ✅ 1. Exploratory Data Analysis (EDA)
- Visualized churn distribution by demographics, contracts, and services
- Identified correlations between churn and contract type, tenure, support usage

### ✅ 2. Feature Engineering
- Created derived features (e.g., average monthly spend per tenure)
- Handled missing and categorical data using encoding and imputation

### ✅ 3. Model Building (Scikit-learn)
- Trained models: Logistic Regression, Random Forest, XGBoost
- Achieved ~85% accuracy with high recall on churn class

### ✅ 4. Deployment (Streamlit)
- Built an interactive web app for live churn prediction
- Input customer attributes and view predicted churn probability

---

## 💡 Key Insights

- Customers on **Month-to-Month contracts** and **without tech support** had the highest churn rates
- **Tenure** and **TotalCharges** were strong predictors of customer loyalty
- Offering **longer contracts** and **better support** can reduce churn

---

## 📷 Screenshots

![Churn Prediction UI](screenshots/streamlit-ui.png)
> Streamlit App Interface for live churn scoring

---

## 🛠️ How to Run the Project

### 1. Clone the Repo
```bash
git clone https://github.com/ShivSingh2208/Customer-Churn-.git
cd Customer-Churn-
