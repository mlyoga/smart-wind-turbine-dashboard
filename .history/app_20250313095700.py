# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import GradientBoostingRegressor, IsolationForest
from sklearn.model_selection import train_test_split
import paho.mqtt.client as mqtt

# Page Config
st.set_page_config(page_title="Smart Wind Turbine Dashboard", page_icon="🌬️", layout="wide")

# Title
st.title("🌬️ Smart Wind Turbine Dashboard")
st.markdown("---")

# Sidebar for user inputs
st.sidebar.header("Configuration")
wind_speed = st.sidebar.slider("Wind Speed (m/s)", 0.0, 25.0, 10.0)
wind_direction = st.sidebar.slider("Wind Direction (degrees)", 0, 360, 90)
turbine_id = st.sidebar.selectbox("Turbine ID", ["Turbine-001", "Turbine-002", "Turbine-003"])

# Load synthetic data
@st.cache_data
def load_data():
    return pd.read_csv("data/synthetic_data.csv")

data = load_data()

# Section 1: AI-Powered Wind Speed & Direction Prediction
st.header("🌪️ AI-Powered Wind Speed & Direction Prediction")

# Train and predict wind speed
X_wind_speed = data[['Wind Speed (m/s)', 'Wind Direction (degrees)']]
y_wind_speed = data['Wind Speed (m/s)']
X_train_speed, X_test_speed, y_train_speed, y_test_speed = train_test_split(X_wind_speed, y_wind_speed, test_size=0.2, random_state=42)
wind_speed_model = GradientBoostingRegressor()
wind_speed_model.fit(X_train_speed, y_train_speed)
predicted_wind_speed = wind_speed_model.predict([[wind_speed, wind_direction]])[0]
st.write(f"Predicted Wind Speed: {predicted_wind_speed:.2f} m/s")

# Section 2: Automatic Blade Angle & Rotational Speed Adjustment
st.header("⚙️ Automatic Blade Angle & Rotational Speed Adjustment")

# Physics-based calculations
optimal_angle = calculate_optimal_angle(wind_direction, wind_speed)
optimal_speed = calculate_optimal_speed(wind_speed)
st.write(f"Optimal Blade Angle: {optimal_angle:.2f} degrees")
st.write(f"Optimal Rotational Speed: {optimal_speed:.2f} RPM")

# Section 3: IoT-Based Remote Monitoring & Control
st.header("📡 IoT-Based Remote Monitoring & Control")

# Simulate IoT integration
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)
client.loop_start()
iot_data = {
    'Wind Speed (m/s)': wind_speed,
    'Wind Direction (degrees)': wind_direction,
    'Power Output (kW)': model.predict([[wind_speed, wind_direction]])[0]
}
client.publish(MQTT_TOPIC, str(iot_data))

# Section 4: Energy Storage Optimization
st.header("🔋 Energy Storage Optimization")

# Battery management logic
battery_level = optimize_battery(model.predict([[wind_speed, wind_direction]])[0], battery_level)
st.write(f"Battery Level: {battery_level:.2f} kWh")

# Section 5: Predictive Maintenance Alerts
st.header("🔧 Predictive Maintenance Alerts")

# Anomaly detection
anomaly_prediction = maintenance_model.predict([[5, 80, 30]])
if anomaly_prediction[0] == -1:
    st.write("⚠️ Maintenance Alert: Anomaly detected in turbine components!")
else:
    st.write("Maintenance Status: Normal")

# Footer
st.markdown("---")
st.write("Developed with Emberglow")