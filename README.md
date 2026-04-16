# Heart-Risk-Prediction
# ❤️ Heart Disease Prediction App

An interactive **Machine Learning web app** built with **Streamlit** that predicts the risk of heart disease based on patient health data.

---

## 🚀 Overview

This project uses a trained **Support Vector Machine (SVM)** model to analyze key medical features and estimate whether a patient is at **high or low risk of heart disease**.

The app provides a simple and user-friendly interface for entering patient details and instantly receiving predictions.

---

## 🧠 Features

* 🎯 Real-time heart disease prediction
* 📊 Clean and interactive UI with Streamlit
* 🧾 Easy input form for patient data
* ⚡ Fast preprocessing using saved transformer & scaler
* ✅ Clear result display (High Risk / Low Risk)

---

## 🏗️ Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **Pandas**
* **Joblib**

---

## 📁 Project Structure

```
├── app.py                # Main Streamlit app
├── SVM_Heart.pkl        # Trained SVM model
├── transformer.pkl      # Data preprocessing transformer
├── scaler.pkl           # Feature scaler
├── columns.pkl          # Model input columns
└── README.md            # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone (https://github.com/Muhammad-Khan-Khichi/Heart-Risk-Prediction).git
cd heart-disease-predictor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 📊 Input Features

The model uses the following medical attributes:

* Age
* Gender
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol Level
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak (ST Depression)
* ST Slope

---

## 🧪 Model Details

* Algorithm: **Support Vector Machine (SVM)**
* Preprocessing:

  * Categorical encoding via transformer
  * Feature scaling using StandardScaler

---

## ⚠️ Disclaimer

This application is for **educational and demonstration purposes only**.
It is **not a substitute for professional medical advice, diagnosis, or treatment**.

---

## 👨‍💻 Author

**Muhammad Khan**

---

## 🌟 Future Improvements

* 📈 Add probability-based risk score
* 🎯 Visual dashboards (charts & gauges)
* 🧠 Model explainability (SHAP)
* 🌐 Deploy online (Streamlit Cloud / Render)

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
