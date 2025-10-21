import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Michaelis-Menten equation
def michaelis_menten(S, Vmax, Km):
    return (Vmax * S) / (Km + S)

# Read data
data = pd.read_csv("enzyme_data.csv")
S = data["Substrate_Concentration_mM"]
v = data["Reaction_Velocity_uM_per_min"]

# Fit the curve
params, _ = curve_fit(michaelis_menten, S, v)
Vmax, Km = params

print(f"Estimated Vmax: {Vmax:.3f}")
print(f"Estimated Km: {Km:.3f}")

# Plot
plt.scatter(S, v, label="Experimental Data", color="blue")
S_fit = np.linspace(0, max(S), 100)
v_fit = michaelis_menten(S_fit, Vmax, Km)
plt.plot(S_fit, v_fit, color="red", label="Fitted Curve")
plt.xlabel("Substrate Concentration [S] (mM)")
plt.ylabel("Reaction Velocity (μM/min)")
plt.title("Enzyme Kinetics Analysis (Michaelis-Menten Plot)")
plt.legend()
plt.grid(True)
plt.show()
