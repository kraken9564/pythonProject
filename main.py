import numpy as np

# Define model parameters
num_evs = 1000
avg_charging_rate = 7 # kWh
charging_duration = 4 # hours
peak_time = 18 # 6pm

# Generate random inputs
num_iterations = 10000
num_evs_dist = np.random.normal(num_evs, 100, num_iterations)
charging_rate_dist = np.random.normal(avg_charging_rate, 1, num_iterations)
charging_duration_dist = np.random.normal(charging_duration, 0.5, num_iterations)
charging_time_dist = np.random.normal(peak_time, 2, num_iterations)

# Run the simulation
total_demand = num_evs_dist * charging_rate_dist * charging_duration_dist
peak_demand = np.max(total_demand)

# Analyze the results
avg_demand = np.mean(total_demand)
std_dev_demand = np.std(total_demand)
prob_peak_demand = np.sum(total_demand >= peak_demand) / num_iterations

import matplotlib.pyplot as plt

# Create a histogram of the total demand distribution
plt.hist(total_demand, bins=50, density=True)

# Add labels and title
plt.xlabel("Total Demand (kWh)")
plt.ylabel("Density")
plt.title("Total Demand Distribution")

# Show the plot
plt.show()
