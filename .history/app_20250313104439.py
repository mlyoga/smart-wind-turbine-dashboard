# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Page Config
st.set_page_config(page_title="Smart Wind Turbine Dashboard", page_icon="🌀", layout="wide")

# Title
st.title("🌀 Smart Wind Turbine Dashboard")
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

# Section 1: Wind Speed & Direction Prediction
st.header("🌪️ Wind Speed & Direction Prediction")

# Train a simple ML model
X = data[['Wind Speed (m/s)', 'Wind Direction (degrees)']]
y = data['Power Output (kW)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Display prediction results
st.write(f"Predicted Power Output: {model.predict([[wind_speed, wind_direction]])[0]:.2f} kW")
st.write(f"Model Mean Squared Error: {mse:.2f}")

# Plot synthetic wind data
fig = px.scatter(data, x='Wind Speed (m/s)', y='Power Output (kW)', color='Wind Direction (degrees)',
                 title="Wind Speed vs. Power Output")
st.plotly_chart(fig, use_container_width=True)

# Section 2: Automatic Blade Angle & Rotational Speed Adjustment
st.header("⚙️ Automatic Blade Angle & Rotational Speed Adjustment")

# Synthetic calculations for optimal settings
optimal_angle = wind_direction * 0.8  # Dummy calculation
optimal_speed = wind_speed * 10  # Dummy calculation
st.write(f"Optimal Blade Angle: {optimal_angle:.2f} degrees")
st.write(f"Optimal Rotational Speed: {optimal_speed:.2f} RPM")

# Section 3: IoT-Based Remote Monitoring & Control
st.header("📡 IoT-Based Remote Monitoring & Control")

# Generate synthetic live data
def generate_live_data():
    return {
        'Wind Speed (m/s)': wind_speed + np.random.uniform(-1, 1),
        'Wind Direction (degrees)': wind_direction + np.random.uniform(-5, 5),
        'Power Output (kW)': model.predict([[wind_speed, wind_direction]])[0] + np.random.uniform(-10, 10)
    }

live_data = generate_live_data()
st.write(f"Monitoring Turbine: {turbine_id}")
st.write("Real-time Data:")
st.table(pd.DataFrame([live_data]))

# Simulate live data updates
if st.button("Refresh Live Data"):
    live_data = generate_live_data()
    st.experimental_rerun()

# Section 4: Energy Storage Optimization
st.header("🔋 Energy Storage Optimization")

# Synthetic battery data
battery_level = np.random.uniform(0, 100)
st.write(f"Battery Level: {battery_level:.2f}%")
st.write("Optimizing energy storage based on predicted power output...")

# Plot battery level over time
battery_history = np.random.uniform(0, 100, 20)  # Synthetic history
fig_battery = px.line(x=range(len(battery_history)), y=battery_history, 
                      labels={'x': 'Time', 'y': 'Battery Level (%)'}, 
                      title="Battery Level Over Time")
st.plotly_chart(fig_battery, use_container_width=True)

# Section 5: Predictive Maintenance Alerts
st.header("🔧 Predictive Maintenance Alerts")

# Synthetic maintenance alerts
maintenance_status = "Normal"
if wind_speed > 20:
    maintenance_status = "⚠️ Warning: High wind speed detected! Inspect turbine blades."
elif battery_level < 20:
    maintenance_status = "⚠️ Warning: Low battery level! Check energy storage system."
st.write(f"Maintenance Status: {maintenance_status}")

# Simulate component wear and tear
component_wear = {
    'Blades': np.random.uniform(0, 100),
    'Gearbox': np.random.uniform(0, 100),
    'Generator': np.random.uniform(0, 100)
}
st.write("Component Wear and Tear:")
st.table(pd.DataFrame([component_wear]))

# Plot wear and tear
fig_wear = px.bar(x=list(component_wear.keys()), y=list(component_wear.values()), 
                 labels={'x': 'Component', 'y': 'Wear (%)'}, 
                 title="Component Wear and Tear")
st.plotly_chart(fig_wear, use_container_width=True)
# Control Buttons
st.header("Turbine Control")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Start Turbine"):
        st.success("Turbine started successfully!")
with col2:
    if st.button("Stop Turbine"):
        st.error("Turbine stopped!")
with col3:
    if st.button("Adjust Blade Angle"):
        st.info("Blade angle adjusted for optimal performance.")
# Footer
st.markdown("---")
st.write("Developed with ❤by Emberglow")