from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("data/cv_5mVs.csv")
OUTPUT_DIR = Path("figures")

SCAN_RATE_MV_S = 5

OUTPUT_DIR.mkdir(exist_ok=True)

data = pd.read_csv(DATA_FILE)

potential_v = data["potential_v"]
current_a = data["current_a"]

plt.figure(figsize=(7, 5))

plt.plot(
    potential_v,
    current_a * 1000,
    color="purple",
    linewidth=2,
    label=f"{SCAN_RATE_MV_S} mV/s",
)

plt.axhline(0, color="black", linewidth=0.8)
plt.xlabel("Potential (V)")
plt.ylabel("Current (mA)")
plt.title("Cyclic Voltammetry of TiO$_2$ Electrode")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "cv_5mVs_curve.png", dpi=300)
plt.show()

print("CV plot saved to figures/cv_5mVs_curve.png")
