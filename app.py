import streamlit as st
import pandas as pd
import joblib
import time

# Load models
model = joblib.load('SVM_Heart.pkl')
transformer = joblib.load('transformer.pkl')
scaler = joblib.load('scaler.pkl')

# Page config
st.set_page_config(page_title="Heart Risk Prediction", page_icon="❤️", layout="wide")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1 style='text-align:center; color:#ff4b4b;'>❤️ Heart Disease Risk Predictor</h1>
<p style='text-align:center;'>AI-powered health screening system</p>
""", unsafe_allow_html=True)

# Layout
left, right = st.columns([2,1])

with left:
    st.markdown("### 🧾 Patient Inputs")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 100, 40)
        gender = st.selectbox("Gender", ['M', 'F'])
        chest_pain = st.selectbox("Chest Pain", ["ATA", "NAP", "TA", "ASY"])
        resting_bp = st.number_input("Resting BP", 80, 200, 120)
        cholesterol = st.number_input("Cholesterol", 100, 600, 200)

    with col2:
        fasting_bs = st.selectbox("Fasting Sugar >120", [0,1])
        resting_ecg = st.selectbox("ECG", ["Normal", "ST", "LVH"])
        max_hr = st.slider("Max HR", 60, 220, 150)
        exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
        oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
        st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    predict_btn = st.button("🔍 Run Prediction")

with right:
    st.markdown("### 📊 Live Health Metrics")

    st.metric("Age", age)
    st.metric("Cholesterol", cholesterol)
    st.metric("Max HR", max_hr)

    st.markdown("---")
    st.info("This AI tool estimates heart disease risk. It is not a medical diagnosis.")

# Prediction
if predict_btn:
    with st.spinner("Analyzing patient data..."):
        time.sleep(1.5)

        raw_input = {
            'Age': age,
            'Sex': gender,
            'ChestPainType': chest_pain,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'RestingECG': resting_ecg,
            'MaxHR': max_hr,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope
        }

        input_df = pd.DataFrame([raw_input])

        transformed_input = transformer.transform(input_df)
        scaled_input = scaler.transform(transformed_input)

        prediction = model.predict(scaled_input)[0]

        try:
            probability = model.predict_proba(scaled_input)[0][1]
        except:
            probability = None

    st.markdown("---")
    st.markdown("## 🧠 Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
        if probability:
            st.metric("Risk Score", f"{round(probability*100,2)}%")
    else:
        st.success("✅ Low Risk of Heart Disease")
        if probability:
            st.metric("Risk Score", f"{round(probability*100,2)}%")

    # Simple visualization
    chart_data = pd.DataFrame({
        "Metric": ["Age", "Cholesterol", "MaxHR"],
        "Value": [age, cholesterol, max_hr]
    })

    st.bar_chart(chart_data.set_index("Metric"))

    st.markdown("---")
    st.caption("Developed by Muhammad Khan | AI Health Dashboard")



