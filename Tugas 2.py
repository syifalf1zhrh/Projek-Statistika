import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from math import pi
from wordcloud import WordCloud
import pandas as pd

# Data kategori harga produk rajutan
kategori = ["< Rp50.000", "Rp50.000–Rp100.000", "Rp100.000–Rp200.000", "> Rp200.000"]
penjualan = [20, 35, 28, 12]

# Tambahan data untuk Dumbbell (before-after, misal bulan Juni vs Juli)
penjualan_juni = [18, 30, 25, 10]
penjualan_juli = penjualan

# Buat file PDF
with PdfPages("Visualisasi_Penjualan_Rajutan.pdf") as pdf:

    # Halaman 1 - Cover
    plt.figure(figsize=(8.5, 11))
    plt.axis("off")
    plt.text(0.5, 0.7, "Analisis Penjualan Produk Rajutan", fontsize=20, ha="center")
    plt.text(0.5, 0.6, "Berdasarkan Kategori Harga", fontsize=16, ha="center")
    plt.text(0.5, 0.5, "Nama: SYIFA ALFI ZAHRAH", fontsize=14, ha="center")
    plt.text(0.5, 0.45, "NIM: 24/544512/SV/25437", fontsize=14, ha="center")
    plt.text(0.5, 0.35, "Tugas Pengantar Statistika", fontsize=12, ha="center")
    pdf.savefig()
    plt.close()

    # 1. Side-by-Side Horizontal Bars (misal perbandingan Juni vs Juli)
    x = np.arange(len(kategori))
    plt.figure(figsize=(8,6))
    plt.barh(x-0.2, penjualan_juni, height=0.4, label="Juni", color="skyblue")
    plt.barh(x+0.2, penjualan_juli, height=0.4, label="Juli", color="orange")
    plt.yticks(x, kategori)
    plt.xlabel("Jumlah Terjual")
    plt.title("Side-by-Side Horizontal Bars")
    plt.legend()
    pdf.savefig()
    plt.close()

    # 2. Radar / Spider chart
    N = len(kategori)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    values = penjualan + penjualan[:1]

    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], kategori)
    ax.plot(angles, values, linewidth=2, linestyle='solid', label="Juli")
    ax.fill(angles, values, 'skyblue', alpha=0.4)
    plt.title("Radar Chart Penjualan Rajutan")
    pdf.savefig()
    plt.close()

    # 3. Stacked Horizontal Bars
    plt.figure(figsize=(8,5))
    plt.barh(kategori, penjualan, color="green")
    plt.title("Stacked Horizontal Bars Penjualan Rajutan")
    plt.xlabel("Jumlah Terjual")
    pdf.savefig()
    plt.close()

    # 4. 100% Stacked (Likert-style)
    total = sum(penjualan)
    persen = [p/total*100 for p in penjualan]
    left = 0
    plt.figure(figsize=(8,2))
    for i in range(len(kategori)):
        plt.barh(["Penjualan (%)"], persen[i], left=left, label=kategori[i])
        left += persen[i]
    plt.title("100% Stacked Horizontal Bars (Likert-style)")
    plt.legend()
    pdf.savefig()
    plt.close()

    # 5. Word Cloud
    text = " ".join([
        "Murah", "Aksesoris", "Rajut", "Tas", "Boneka", "Sweater", 
        "Dompet", "Premium", "Favorit", "Trend", "Terjangkau", "Kualitas"
    ])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(8,6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud Produk Rajutan")
    pdf.savefig()
    plt.close()

    # 6. Dumbbell Chart (Before-After: Juni vs Juli)
    df = pd.DataFrame({
        "Kategori": kategori,
        "Juni": penjualan_juni,
        "Juli": penjualan_juli
    })
    plt.figure(figsize=(8,6))
    for i in range(len(df)):
        plt.plot([df["Juni"][i], df["Juli"][i]], [i, i], color="grey", lw=2)
        plt.scatter(df["Juni"][i], i, color="skyblue", s=100, label="Juni" if i==0 else "")
        plt.scatter(df["Juli"][i], i, color="orange", s=100, label="Juli" if i==0 else "")
    plt.yticks(range(len(df)), df["Kategori"])
    plt.xlabel("Jumlah Terjual")
    plt.title("Dumbbell Chart (Juni vs Juli)")
    plt.legend()
    pdf.savefig()
    plt.close()

print("File berhasil disimpan sebagai Visualisasi_Penjualan_Rajutan.pdf")
