import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# Page Config
st.set_page_config(page_title="Smart Wind Turbine Dashboard", page_icon="🌬️", layout="wide")

# Title
st.title("📡 IoT-Based Remote Monitoring & Control")
st.markdown("---")

# Sidebar for user inputs
st.sidebar.header("Configuration")
turbine_id = st.sidebar.selectbox("Turbine ID", ["Turbine-001", "Turbine-002", "Turbine-003"])

# Simulate Real-Time Data
def generate_live_data():
    return {
        'Wind Speed (m/s)': np.random.uniform(0, 25),
        'Wind Direction (degrees)': np.random.uniform(0, 360),
        'Power Output (kW)': np.random.uniform(0, 500)
    }

# Display Turbine Status
turbine_status = "Running" if np.random.random() > 0.1 else "Stopped"
st.write(f"**Turbine Status:** {turbine_status}")

# Real-Time Data Section
st.header("Real-Time Data")

# Add a refresh button
if st.button("Refresh Data"):
    live_data = generate_live_data()
    st.experimental_rerun()

# Display real-time data in a table
live_data = generate_live_data()
st.table(pd.DataFrame([live_data]))

# Visualizations
st.header("Visualizations")

# Line chart for wind speed over time
st.subheader("Wind Speed Over Time")
wind_speed_history = np.random.uniform(0, 25, 10)  # Simulated history
fig_wind_speed = px.line(x=range(len(wind_speed_history)), y=wind_speed_history, 
                         labels={'x': 'Time', 'y': 'Wind Speed (m/s)'}, 
                         title="Wind Speed Over Time")
st.plotly_chart(fig_wind_speed, use_container_width=True)

# Gauge for power output
st.subheader("Power Output Gauge")
power_output = live_data['Power Output (kW)']
fig_gauge = px.pie(values=[power_output, 500 - power_output], names=['Power Output', 'Remaining'], 
                   title=f"Power Output: {power_output:.2f} kW", hole=0.6)
fig_gauge.update_traces(textinfo='none', hoverinfo='label+percent')
st.plotly_chart(fig_gauge, use_container_width=True)

# Alerts and Notifications
st.header("Alerts and Notifications")
if live_data['Wind Speed (m/s)'] > 20:
    st.error("⚠️ High Wind Speed Alert: Wind speed exceeds safe limits!")
if live_data['Power Output (kW)'] < 100:
    st.warning("⚠️ Low Power Output Alert: Power output is below expected levels!")

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