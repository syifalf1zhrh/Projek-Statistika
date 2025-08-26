import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Data kategori harga produk rajutan
kategori_harga = ["< Rp50.000", "Rp50.000 – Rp100.000", "Rp100.000 – Rp200.000", "> Rp200.000"]
frekuensi = [20, 35, 28, 12]

# Narasi
narasi = """
Laporan Penjualan Rajutan Berdasarkan Kategori Harga

Data penjualan rajutan bulan Juli dikelompokkan berdasarkan kategori harga:

< Rp50.000             : 20 unit
Rp50.000 – Rp100.000   : 35 unit
Rp100.000 – Rp200.000  : 28 unit
> Rp200.000            : 12 unit

Analisis:
Produk dengan harga Rp50.000 – Rp100.000 memiliki penjualan tertinggi (35 unit), 
menunjukkan segmen harga menengah paling diminati konsumen. Produk di atas Rp200.000 
memiliki penjualan paling rendah (12 unit), menandakan segmen premium masih terbatas peminatnya. 
Total penjualan bulan Juli adalah 95 unit.
"""

# Buat file PDF
with PdfPages("penjualan_rajutan_kategori_harga.pdf") as pdf:

    # Halaman 1 - Narasi
    plt.figure(figsize=(8.5, 11))
    plt.axis("off")
    plt.text(0, 1, narasi, fontsize=12, va="top")
    pdf.savefig()
    plt.close()

    # Halaman 2 - Grafik Bar
    plt.figure(figsize=(6,4))
    plt.bar(kategori_harga, frekuensi, color="skyblue", edgecolor="black")
    plt.title("Grafik Bar Penjualan Rajutan Berdasarkan Kategori Harga")
    plt.xlabel("Kategori Harga")
    plt.ylabel("Jumlah Terjual")
    plt.tight_layout()
    pdf.savefig()  # simpan ke PDF
    plt.show()     # tampilkan di layar
    plt.close()

    # Halaman 3 - Grafik Line
    plt.figure(figsize=(6,4))
    plt.plot(kategori_harga, frekuensi, marker="o", color="green", linestyle="-")
    plt.title("Grafik Line Penjualan Rajutan Berdasarkan Kategori Harga")
    plt.xlabel("Kategori Harga")
    plt.ylabel("Jumlah Terjual")
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.show()
    plt.close()

    # Halaman 4 - Grafik Pie
    plt.figure(figsize=(6,6))
    plt.pie(frekuensi, labels=kategori_harga, autopct="%1.1f%%", startangle=90)
    plt.title("Grafik Pie Penjualan Rajutan Berdasarkan Kategori Harga")
    plt.tight_layout()
    pdf.savefig()
    plt.show()
    plt.close()

print("File berhasil disimpan sebagai penjualan_rajutan_kategori_harga.pdf")
