import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ============================================================
# 1. Generate Data Cuaca 14 Hari (integer / tanpa koma)
# ============================================================
np.random.seed(42)   # agar hasil sama setiap run
n = 14
weather_2w = pd.DataFrame({
    'Day': range(1, n+1),
    'MaxTemp (°C)': np.random.randint(28, 38, n),   # suhu max 28–37
    'MinTemp (°C)': np.random.randint(20, 28, n),   # suhu min 20–27
    'Humidity (%)': np.random.randint(55, 90, n),   # kelembapan 55–89
    'Rainfall (mm)': np.random.randint(0, 20, n),   # curah hujan 0–19
    'WindSpeed (km/h)': np.random.randint(5, 25, n) # angin 5–24
})

print("=== Data Cuaca 14 Hari (Integer) ===")
print(weather_2w.to_string(index=False))

# ============================================================
# 2. Hitung Statistik Deskriptif
# ============================================================
mode_vals = [
    stats.mode(weather_2w[col], keepdims=True)[0][0]
    for col in weather_2w.columns[1:]
]
summary = weather_2w.drop(columns='Day').agg(['mean','median','var','std']).round(0).astype(int).T
summary.columns = ['Mean','Median','Variance','Std Dev']
summary['Mode'] = mode_vals

print("\n=== Ringkasan Statistik ===")
print(summary)

# ============================================================
# 3. Box-and-Whisker Plot Berwarna
# ============================================================
data = weather_2w.drop(columns='Day')

plt.figure(figsize=(10,6))
plt.boxplot(
    data.values,
    patch_artist=True,  # agar box bisa diwarnai
    labels=data.columns,
    boxprops=dict(facecolor='skyblue', color='navy'),    # warna kotak & outline
    medianprops=dict(color='red', linewidth=2),          # garis median
    whiskerprops=dict(color='green', linewidth=1.5),     # whisker
    capprops=dict(color='purple', linewidth=1.5),        # ujung whisker
    flierprops=dict(marker='o', markerfacecolor='orange',
                    markeredgecolor='darkorange', markersize=6)  # outlier
)

plt.title('Box and Whisker Plot – Data Cuaca 14 Hari')
plt.ylabel('Nilai')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
