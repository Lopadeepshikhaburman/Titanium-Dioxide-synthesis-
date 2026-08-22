from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("data/gcd_example.csv")
OUTPUT_DIR = Path("figures")

ACTIVE_MASS_G = 0.002
DISCHARGE_CURRENT_A = 0.001
VOLTAGE_WINDOW_V = 1.0

OUTPUT_DIR.mkdir(exist_ok=True)

data = pd.read_csv(DATA_FILE)

time_s = data["time_s"]
voltage_v = data["voltage_v"]

peak_index = voltage_v.idxmax()

discharge_time_s = time_s.iloc[-1] - time_s.loc[peak_index]

specific_capacitance_f_g = (
    DISCHARGE_CURRENT_A * discharge_time_s
) / (
    ACTIVE_MASS_G * VOLTAGE_WINDOW_V
)

energy_density_wh_kg = (
    specific_capacitance_f_g * VOLTAGE_WINDOW_V**2
) / 7.2

power_density_w_kg = (
    energy_density_wh_kg * 3600
) / discharge_time_s

results = pd.DataFrame(
    {
        "metric": [
            "Active material mass",
            "Discharge current",
            "Voltage window",
            "Discharge time",
            "Specific capacitance",
            "Energy density",
            "Power density",
        ],
        "value": [
            ACTIVE_MASS_G,
            DISCHARGE_CURRENT_A,
            VOLTAGE_WINDOW_V,
            discharge_time_s,
            specific_capacitance_f_g,
            energy_density_wh_kg,
            power_density_w_kg,
        ],
        "unit": [
            "g",
            "A",
            "V",
            "s",
            "F/g",
            "Wh/kg",
            "W/kg",
        ],
    }
)

results.to_csv(OUTPUT_DIR / "gcd_results.csv", index=False)

plt.figure(figsize=(7, 5))
plt.plot(time_s, voltage_v, color="darkblue", linewidth=2)
plt.scatter(
    time_s.loc[peak_index],
    voltage_v.loc[peak_index],
    color="crimson",
    label="Start of discharge",
)
plt.xlabel("Time (s)")
plt.ylabel("Potential (V)")
plt.title("GCD Curve of TiO$_2$ Electrode")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "gcd_curve.png", dpi=300)
plt.show()

print(results.to_string(index=False))
