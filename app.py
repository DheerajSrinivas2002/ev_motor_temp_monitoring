import streamlit as st
import joblib
import json
import numpy as np

# Load model and features
model = joblib.load('pm_temperature_model.pkl')
with open('features.json', 'r') as f:
    features = json.load(f)

# App title
st.title("EV Motor PM Temperature Predictor")
st.markdown("Predict permanent magnet temperature from motor sensor readings")

st.sidebar.header("Input Sensor Values")

# Input sliders
coolant = st.sidebar.slider("Coolant Temperature (°C)", 10.0, 102.0, 36.0)
motor_speed = st.sidebar.slider("Motor Speed (rpm)", -276.0, 6001.0, 2202.0)
ambient = st.sidebar.slider("Ambient Temperature (°C)", 8.0, 31.0, 25.0)
u_q = st.sidebar.slider("Voltage Q-axis (u_q)", -26.0, 134.0, 54.0)
u_d = st.sidebar.slider("Voltage D-axis (u_d)", -132.0, 132.0, -25.0)
i_d = st.sidebar.slider("Current D-axis (i_d)", -279.0, 1.0, -69.0)
i_q = st.sidebar.slider("Current Q-axis (i_q)", -294.0, 302.0, 37.0)
torque = st.sidebar.slider("Torque (Nm)", -247.0, 262.0, 31.0)

# Build input array in correct feature order
input_data = np.array([[coolant, motor_speed, ambient, u_q, u_d, i_d, i_q, torque]])

# Predict
prediction = model.predict(input_data)[0]

# Display result
st.metric(
    label="Predicted PM Temperature",
    value=f"{prediction:.1f} °C"
)

# Warning if too hot
if prediction > 100:
    st.error("CRITICAL — Magnet temperature dangerously high!")
elif prediction > 80:
    st.warning("WARNING — Temperature approaching safe limit")
else:
    st.success("Temperature within safe operating range")