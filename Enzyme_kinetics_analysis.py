# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Example data (substrate concentration vs reaction rate)
substrate_conc = np.array([])  # Add substrate concentrations [S]
reaction_rate = np.array([])   # Add corresponding reaction rates v

# Create smooth curve for illustration (not fitted)
S_fit = np.linspace(0, 0, 100)  # Adjust range as needed
Vmax = 0  # Define your Vmax
Km = 0    # Define your Km
v_fit = (Vmax * S_fit) / (Km + S_fit)

# Plot
plt.figure(figsize=(8,5))
plt.scatter(substrate_conc, reaction_rate, color='blue', label='Experimental Data', s=60)
plt.plot(S_fit, v_fit, color='red', linewidth=2, label='Michaelis-Menten Curve')

# Labels and title
plt.title('Enzyme Kinetics: Michaelis-Menten Plot', fontsize=14)
plt.xlabel('Substrate Concentration [S] (mM)', fontsize=12)
plt.ylabel('Reaction Rate v (µM/min)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
