# generate_synthetic_data.py
import pandas as pd
import numpy as np
import os

# Create the 'data' directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Generate synthetic data
np.random.seed(42)  # For reproducibility
num_samples = 100  # Number of data points

# Random wind speeds between 0 and 25 m/s
wind_speed = np.random.uniform(0, 25, num_samples)

# Random wind directions between 0 and 360 degrees
wind_direction = np.random.uniform(0, 360, num_samples)

# Random power outputs between 0 and 500 kW (dependent on wind speed and direction)
power_output = np.random.uniform(0, 500, num_samples)

# Create a DataFrame
data = pd.DataFrame({
    'Wind Speed (m/s)': wind_speed,
    'Wind Direction (degrees)': wind_direction,
    'Power Output (kW)': power_output
})

# Save the data to a CSV file
data.to_csv("data/synthetic_data.csv", index=False)
print("Synthetic data saved to data/synthetic_data.csv")