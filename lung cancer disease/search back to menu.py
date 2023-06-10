# Search + Deskripsi
# binery search deskripsi label text
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Product:
    def __init__(self, name, image_path, price, additional_info):
        self.name = name
        self.image_path = image_path
        self.price = price
        self.additional_info = additional_info

class KumpulanProduk(tk.Tk):
    def __init__(self, products):
        super().__init__()
        self.title("Biner Search Product")
        self.products = products

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_products)

        self.entry_search = ttk.Entry(self, textvariable=self.search_var)
        self.entry_search.pack(fill=tk.NONE, padx=10, pady=10)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.product_frame = ttk.Frame(self.canvas)
        self.product_frame.pack()

        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.product_frame, anchor=tk.NW)

        self.display_products()

        self.product_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.cart = []

    def filter_products(self, *args):
        query = self.search_var.get().lower()
        filtered_products = [product for product in self.products if query in product.name.lower()]
        self.display_products(filtered_products)

    def add_to_cart(self, product):
        print(f"{product.name} GO TO DESCRIPTION!")

    def update_cart(self):
        self.cart_label.configure(text=f"({len(self.cart)} items)")

    def display_products(self, products=None):
        if products is None:
            products = self.products

        for widget in self.product_frame.winfo_children():
            widget.destroy()

        num_cols = 6
        row = 0
        col = 0

        for product in products:
            product_frame = ttk.Frame(self.product_frame)
            product_frame.grid(row=row, column=col, padx=15, pady=15)

            # Resize the image
            image = Image.open(product.image_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            image_label = ttk.Label(product_frame, image=photo)
            image_label.image = photo  # save a reference to the image
            image_label.pack()

            name_label = ttk.Label(product_frame, text=product.name)
            name_label.pack()

            price_label = ttk.Label(product_frame, text=f"Price: {product.price:,}")
            price_label.pack()

            button = ttk.Button(product_frame, text="REVIEW", command=lambda p=product: self.review_product(p))
            button.pack()

            col += 1
            if col == num_cols:
                col = 0
                row += 1

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.product_frame, width=event.width)

    def review_product(self, product):
        review_page = ReviewPage(self, product)
        review_page.pack()
        self.product_frame.pack_forget()

    def back_to_main_page(self):
        self.product_frame.pack()
        self.display_products()

    def destroy_review_page(self, review_page):
        review_page.destroy()
        self.back_to_main_page()


class ReviewPage(ttk.Frame):
    def __init__(self, master, product):
        super().__init__(master)
        self.product = product

        name_label = ttk.Label(self, text=product.name)
        name_label.pack(pady=10)

        # Add additional info
        additional_info_label = ttk.Label(self, text="Additional Information:")
        additional_info_label.pack()

        for info in product.additional_info:
            info_label = ttk.Label(self, text=info)
            info_label.pack()

        back_button = ttk.Button(self, text="Back", command=self.back_to_main_page)
        back_button.pack(pady=10)

    def back_to_main_page(self):
        self.master.destroy_review_page(self)


if __name__ == "__main__":
    products = [
        Product('Mi 37W Dual-Port Car Charger', 'Mi 37W Dual-Port Car Charger.png', 109000,
                [
                    "Nomor model = CCO6ZM",
                    "Output = USB-A",
                    "Parameter input = 12V-24V=4A",
                    "Parameter output = USB1: 5V-2A",
                    "USB2: 5V=3A 9V=3A 12V=2.25A 20V= 1.35A",
                    "Dimensi produk = 74.7 x 30.8 x 30.8mm"
                ]),

        Product('Mi 360 Camera (1080p)', 'Mi 360° Camera (1080p).png', 449000,
                [
                    "Model",
                    "MJSXJ10CM",
                    "Apertur",
                    "F2.1",
                    "Resolusi",
                    "1920x1080",
                    "Memori yang dapat ditambah",
                    "Kartu Micro SD (hingga 32 GB)",
                    "Suhu pengoperasian",
                    "-10℃一40℃",
                    "Konektivitas nirkabel",
                    "Wi-Fi IEEE 802.11b/g/n, 2.4 GHz",
                    "Berat netto",
                    "254 g",
                    "Input daya",
                    "5V/2A",
                ]),

        Product('Mi Curved Gaming Monitior 34', 'Mi Curved Gaming Monitor 34_.png', 5599000,
                [
                    "Spesifikasi Layar",
                    "Resolusi: 3440 x 1440",
                    "Kelengkungan layar: 1500R",
                    "Waktu respons: 4 mdtk (Waktu respons skala abu-abu)",
                    "Warna: 16,7 juta (8-bit)",
                    "Kecerahan: 300 cd/m²",
                    "Layar: 21:9",
                    "Refresh rate: 144 Hz",
                    "Gamut warna: 121% SRGB",
                    "Rasio kontras: 3000:1 (TIPIKAL)",
                    "Mode jendela",
                    "Satu jendela",
                    "Layar terpisah kiri/kanan",
                    "Mode gambar dalam gambar",
                ]),

        Product('Mi Desktop Monitor 27”', 'Mi Desktop Monitor 27”.png', 1699000,
                [
                    "No. model produkRMMNT27NF",
                    "Input daya12V, 2A",
                    "Daya terukur*Maks. 24 W",
                    "Ukuran layar27 inci",
                    "Ukuran layar (diagonal)685,98 mm",
                    "Dot pitch0,3114 x 0,3114 mm",
                    "Kecerahan300 cd/m² (UMUM)",
                    "Kontras1000:1 (UMUM)",
                    "Kontras dinamis1000000:1",
                    "Jumlah warna16,7 juta",
                    "Rasio aspek16:9",
                    "Waktu respons6 ms (GTG)",
                    "Resolusi maksimum1920x1080",
                    "Resolusi yang disarankan1920x1080",
                    "Refresh rate maksimum75 Hz",
                    "Refresh rate yang disarankan60 Hz",
                    "Dimensi613,2 (P) x 205,3 (L) x 476,0 (T) mm",
                ]),

        Product('Mi LCD Writing Tablet 13.5"', 'Mi LCD Writing Tablet 13.5&quot.png', 2699000,
                
                [
                    "Nama produk",
                    "Mi LCD Writing Tablet 13,5",
                    "Model produk",
                    "XMXHB02WC",
                    "Baterai",
                    "Sel kancing (CR2025)",
                    "Dimensi produk",
                    "318 mm x 225 mm x 7 mm 0,345 kg",
                    "Berat netto",
                    "0,345 kg (termasuk baterai tipe",
                    "sel kancing)",
                    "Bahan utama",
                    "Lapisan film lembut LCD yang",
                    "terbuat dari polimer padat ABS",
                ]),

        Product('Mi Robot Vacuum-Mop 2 Lite', 'Mi Robot Vacuum-Mop 2 Lite.png', 2799000,
                [
                    "ModelMJSTL",
                    "Dimensi Item353 x 81,3 mm",
                    "Daya Terukur35 W",
                    "Tegangan Terukur14,4 V⎓",
                    "Berat Bersih3,1 kg",
                    "Kapasitas Baterai2500 mAh (kapasitas terukur)",
                    "2600 mAh (kapasitas nominal)",
                    "ModelCDZMJSTL",
                    "Input Tetapan100-240 V ~ 50/60 Hz 0,6 A",
                    "Output Terukur20 V ⎓ 1,2 A",
                    "Dimensi Item150 x 135 x 97,4 mm",
                ]),

        Product('Mi Router 4C', 'Mi Router 4C.png', 199000,
                [
                    "ProsesorMT7628DA",
                    "Memori internal64MB DDR2",
                    "2.4GhzLNA dan PA terintegrasi",
                    "5GHzTidak didukung",
                    "Disipasi panasPanas alami",
                    "Kelembapan pengoperasian:10-90% RH (tanpa kondensasi)",
                    "Kelembapan penyimpanan:5-90% RH (tanpa kondensasi)",
                    "Standar protokolIEEE 802.11b/g/nIEEE 802.3/3u",
                    "ROM16MB NorFlash",
                    "Wi-Fi 2.4GHz2.4GHz Wi-Fi2x2",
                    "(mendukung protokol IEEE 802.11N, kecepatan maksimum 300 Mbps)",
                    "Wi-Fi 5GHzTidak didukung",
                    "Antena4x antena band tunggal eksternal",
                ]),
        Product('Mi Smart Air Fryer (3.5L)', 'Mi Smart Air Fryer (3.5L).png', 1199000,
                [
                    "ModelMAF02",
                    "Tegangan Terukur220-240 V",
                    "Frekuensi Terukur50-60 Hz",
                    "Berat Bersih3,9 kg",
                    "Berat Kotor5,2 kg",
                    "Daya Terukur1500 W",
                    "Volume Terukur3,5 L",
                    "Bahan KeranjangLogam Alclad",
                ]),
        Product('Mi TV 4 43', 'Mi TV 4 43.png', 3599000,
                [
                    "FHD tampilan",
                    "2x Stereo Speaker 8W",
                    "PatchWall 3.0 dengan Konten lebih dari 700.000 Jam",
                    "Android TV Google Assistant",
                    "Penghemat Data",
                    "FHD",
                    "Resolusi:1920 x 1080",
                    "Sudut pandang: 178°",
                    "Refresh rate: 60Hz",
                    "Lampu latar:: DLED",
                    "Powerful speaker",
                    "Daya audio: 2 x 8W 8ohm",
                    "CPU: Amlogic Cortex A53 quad-core",
                    "RAM: 1GB DDR",
                    "GPU: Mali-450 MP3",
                    "Penyimpanan: 8GB eMMC",
                ]),
        Product('Mi TV 4 55', 'Mi TV 4 55.png', 5999000,
                [
                    "Layar 4K HDR",
                    "2x Stereo Speaker 10W",
                    "PatchWall 3.0 dengan Konten lebih dari 700.000 Jam",
                    "Android TV Google Assistant",
                    "Penghemat Data",
                    "Resolusi: 3840 x 2160",
                    "Sudut pandang: 178°",
                    "Refresh rate: 60Hz",
                    "Lampu latar: DLED",
                    "CPU: Amlogic Cortex A53 quad-core",
                    "RAM: 2GB DDR",
                    "GPU: Mali-450 MP3",
                    "Penyimpanan: 8GB eMMC",
                ]),

        Product('Mi TV Stick', 'Mi TV Stick.png', 599000,
                [
                    "Resolusi output",
                    "1080P (1920x1080@60fps)",
                    "RAM",
                    "1GB",
                    "CPU",
                    "Quad-core Cortex-A53",
                    "Memori Penyimpanan",
                    "8GB",
                    "GPU",
                    "ARM Mali-450",
                    "Sistem operasi",
                    "Android 9.0",
                    "Wi-Fi",
                    "802.11a/b/g/n/ac 2.4GHz/5GHz",
                    "Bluetooth",
                    "4.2",
                ]),
        Product('Mi Vacuum Cleaner Light', 'Mi Vacuum Cleaner Light.png', 1499000,
                [
                    "Nama produk21,6 V",
                    "Tegangan operasi Mi Vacuum Cleaner Light",
                    "Daya operasi 220 W",
                    "Kapasitas baterai lithium 2500 mAh",
                    "Waktu kerja (mode standar/mode MAX)45 mnt/",
                    "13 mnt (tanpa sikat ground listrik)",
                    "Tegangan pengisian daya26,0 V",
                    "Pengisian daya arus kecil0,5 A",
                    "Durasi pengisian daya Kira-kira 5 jam",
                    "Berat Kira-kira 2,3kg",
                    "Kebisingan≤ 79 dB",
                    "Dimensi 240 x 148 x 1132 mm",
                ]),
        Product('Mi Vacuum Cleaner Mini.jpg', 'Mi Vacuum Cleaner Mini.jpg.png', 649000,
                [
                    "Nama produk Mi Vacuum Cleaner Mini",
                    "Berat bersih produk Sekitar 0,5 kg (unit utama)",
                    "Daya Terukur 40W",
                    "Dimensi Produk 267 x 55 x 55 mm",
                    "Tegangan pengenal 10,8V",
                ]),

        Product('Mi Watch Charging Dock', 'Mi Watch Charging Dock.png', 69000,
                [
                    "Nama produk",
                    "Mi Watch Charging Dock",
                    "Material produk",
                    "PC + ABS",
                    "Ukuran produk",
                    "40,3x40,3x9,8 mm",
                ]),

        Product('Mi WiFi Range Extender AC1200', 'Mi WiFi Range Extender AC1200.png', 249000,
                [
                    "ModelRA75",
                    "StandarIEEE 802.11ac/n/a 5GHz, IEEE 802.11n/b/g 2,4GHz",
                    "Kecepatan WiFi5 GHz: 867Mbps (802.11ac, 2*2 @80MHz)" 
                    "2,4 GHz: 300Mbps (802.11n, 2*2 @40MHz)",
                    "ModeMode Range Extender, Mode Access Point",
                    "Keamanan NirkabelWPA-PSK / WPA2-PSK",
                    "Daya Transmisi<20 dBm (2,4 GHz), <23 dBm (5 GHz)",
                    "RAM64MB",
                    "PortPort Ethernet 1*10/100Mbps",
                    "TombolTombol WPS, Tombol Reset",
                    "Input100~240V, 50/60Hz, 0,3A",
                    "Dimensi84x100x82mm*",
                ]),
        Product('Mi Wireless Switch', 'Mi Wireless Switch.png', 99000,
                [
                    "No. model produk",
                    "WXKGO1LM",
                    "Dimensi produk",
                    "50 x 50 x 13 mm",
                    "Konektivitas nirkabel",
                    "Zigbee",
                    "Spesifikasi baterai",
                    "CR2032",
                    "Suhu pengoperasian",
                    "-10°C hingga +50°C",
                    "Kelembapan kerja",
                    "0-95% RH, non-condensasi",
                ]),
        Product('POCO F4 GT', 'POCO F4 GT.png', 7999000,
                [
                    "RAM LPDDR5 + Penyimpanan UFS3.1",
                    "Tinggi: 162,5 mm",
                    "Lebar: 76,7 mm",
                    "Ketebalan: 8,5 mm",
                    "Berat: 210 g",
                    "Snapdragon® 8 Gen 1",
                    "Proses manufaktur 4nm",
                    "CPU: CPU Octa-core Qualcomm® Kryo™, hingga 3,0 GHz",
                    "GPU: GPU Qualcomm® Adreno™",
                    "AI: Qualcomm® AI Engine Generasi ke-7",
                    "Modem Snapdragon® X65 5G",
                    "LiquidCool Technology 3.0",
                    "DotDisplay AMOLED datar 6,67",
                    "Resolusi: FHD+ 2400 x 1080",
                    "Rasio aspek: 20:9",
                    "Refresh rate: Hingga 120 Hz",
                ]),
        Product('POCO F4', 'POCO F4.png', 5199000,
                [
                    "LPDDR5+ UFS 3.1",
                    "Tinggi: 163,2 mm",
                    "Lebar: 75,95 mm",
                    "Ketebalan: 7,7 mm",
                    "Berat: 195 g",
                    "Snapdragon® 870",
                    "CPU: CPUI Octa-core® Qualcomm Kryo™ 585",
                    "Proses manufaktur 7nm 1x Prime core ",
                    "berbasis A77, 3,2 GHz 3x Gold core",
                    "berbasis A77, 2,42 GHz 4x Silver core" ,
                    "berbasis A55, 1,8 GHz",
                    "GPU: GPU Qualcomm® Adreno™ 650",
                    "Modem X55 untuk konektivitas 5G" ,
                    "AMOLED 120 Hz 6,67”",
                    "DotDisplay ultra-mungil 2.76 mm",
                    "20:9, 2400x1080 FHD+",
                    "DCI-P3 100% (standar)",

                ]),
        Product('poco M4 pro', 'poco M4 pro.png', 3399000,
                [
                    "RAM LPDDR4X + Penyimpanan UFS2.2",
                    "Tinggi: 159,87 mm",
                    "Lebar: 73,87 mm",
                    "Ketebalan: 8,09 mm",
                    "Berat: 179,5 g",
                    "MediaTek Helio G96",
                    "CPU: CPU octa-core, hingga 2,05 GHz",
                    "GPU: Mali-G57 MC2",
                    "Baterai 5000mAh (typ)",
                    "Pengisian cepat 33W Pro",
                    "DotDisplay AMOLED FHD+ 6,43FHD+" ,
                    "2400x1080Rasio kontras: 4.500.000:1",
                    "Tingkat kecerahan: 2048",
                    "Refresh rate: 90 Hz",
                    "Touch sampling rate: 180 Hz",
                    "Sunlight displaySGS Eye Care DisplaySGS" ,
                    "Seamless Display",
                ]),
        Product('POCO M5', 'POCO M5.png', 2299000,
                [
                    "Tinggi: 163,99 mm",
                    "Lebar: 76,09 mm",
                    "Ketebalan: 8,9 mm",
                    "Berat: 201 g",
                    "MediaTek Helio G99",
                    "Proses manufaktur 6nm",
                    "CPU: CPU octa-core, hingga 2,2 GHz",
                    "GPU: Arm Mali-G57 MC2",
                    "Layar 6,58 FHD+ DotDrop" ,
                    "Resolusi: FHD+ 2408 x 1080",
                    "Rasio aspek: 20:9",
                    "Refresh rate: 30 / 60 / 90 Hz",
                    "Touch sampling rate: 240 Hz",
                    "Kecerahan: 500 nit (HBM)",
                    "Rasio kontras: 1500:1",
                    "Corning® Gorilla® Glass",
                ]),
        Product('POCO M5s', 'POCO M5s.png', 2599000,
                [
                    "MediaTek Helio G95CPU:",
                    "CPU octa-core, hingga 2,05 GHz",
                    "GPU: Arm Mali-G76 MC4",
                    "Tinggi: 160,46 mm",
                    "Lebar: 74,5 mm",
                    "Ketebalan: 8,29 mm",
                    "Berat: 178,8 g",
                    "DotDisplay AMOLED 6,43”",
                    "Resolusi: FHD+, 2400 x 1080",
                    "PPI: 409",
                    "Kecerahan:",
                    "Mode kecerahan tinggi: 700 nit",
                    "Kecerahan puncak 1100 nit",
                    "Rasio kontras: 4500000:1",
                    "Peredupan DCSunlight display",
                    "Mode Baca",
                    "Corning® Gorilla® Glass",
                ]),
        Product('POCO X5 5G', 'POCO X5 5G.png', 3499000,
                [
                    "LPDDR4X + UFS2.2",
                    "Penyimpanan dapat diperbesar hingga 1TB",
                    "Tinggi: 165,88 mm",
                    "Lebar: 76,21 mm",
                    "Ketebalan: 7,98 mm",
                    "Berat: 189 g",
                    "Snapdragon® 695 5G Mobile Platform",
                    "CPU: CPU octa-core, hingga 2,2 GHz",
                    "GPU: Qualcomm® Adreno™ 619",
                    "5.000 mAh (standar)",
                    "Pengisian daya cepat 33 W",
                    "6.67' FHD+ AMOLED DotDisplay",
                    "Refresh rate: Hingga 120 Hz",
                    "Kecerahan: 700 nit (HBM), 1.200 nit (maksimal)Rasio kontras: 4.500.000:1",
                    "Resolusi: 2400 x 1080Gamut warna luas DCI-P3",
                ]),
        Product('Redmi 10 2022', 'Redmi 10 2022.png', 2299000,
                [
                    "LPDDR4X +eMMC",
                    "Tinggi: 161,95 mm",
                    "Lebar: 75,53 mm",
                    "Ketebalan: 8,92 mm",
                    "Berat: 181 g",
                    "MediaTek Helio G882 x Arm Cortex-A75 @ 2",
                    "GHz6 x Arm Cortex-A55 @ 1,8 GHzProses",
                    "manufaktur 12 nmGPU Arm Mali-G52",
                    "DotDisplay FHD+ 6,5",
                    "Refresh rate: 90 Hz",
                    "AdaptiveSync: 45/60/90 Hz",
                    "2400 x 1080, 405 ppi",
                    "Sunlight display",
                    "Mode baca 3.0Corning® Gorilla® Glass 3",
                    "Baterai 5000 mAh (standar)",
                    "Pengisian daya cepat 18 W",
                    "Reverse charging 9 W",
                ]),
        Product('Redmi Buds 3 Pro', 'Redmi Buds 3 Pro.png', 699000,
                [
                    "No. model produkTWSEJ01ZM",
                    "Waktu pengisian daya earbudSekitar 1 jam",
                    "Konektivitas nirkabelBluetooth 5.2",
                    "Waktu pengisian dengan dudukan pengisian daya",
                    "Sekitar 2,5 jam(pengisian daya dengan kabel)",
                    "Berat bersih satu earbudSekitar 4,9 g",
                    "Dimensi earbud25,4*20,3*21,3 mm",
                    "Berat total termasuk dudukan pengisian dayaSekitar 55 g",
                    "Dimensi dudukan pengisian daya65*48*26 mm",
                    "Impedansi speaker32 Ω",
                ]),

        Product('Redmi buds 4 Pro', 'Redmi buds 4 Pro.png', 949000,
                [
                    "No. model produkM2132E1",
                    "Parameter input earbudMAKS. 5,25 V ⎓ 160 mA (satu earbud)",
                    "Parameter input dudukan pengisian dayaMAKS. 5 V = 0,5 A",
                    "Port pengisian dayaUSB-C",
                    "Konektivitas nirkabelBluetooth® 5.3",
                    "Profil BluetoothBluetooth®Low Energy/HFP/A2DP/AVRCP",
                    "Jarak operasional10 m (ruang terbuka tanpa penghalang)",
                    "Impedansi speaker24 Ω",
                ]),
        Product('Redmi buds 4', 'Redmi buds 4.png', 549000,
                [
                    "Nomor model produk:M2137E1",
                    "Parameter input earbud:5V ⎓ 100mA",
                    "Parameter input kasing pengisi daya: 5V ⎓ 450mA",
                    "Koneksi nirkabel: Bluetooth 5.2 HSP, HFP",
                    "Protokol Bluetooth: HSP、HFP、A2DP、AVRCP",
                    "Jarak operasi: 10m (ruang terbuka bebas hambatan)",
                    "Berat bersih earbud tunggal: Kira-kira. 4,5g",
                    "Berat total termasuk wadah pengisi daya: Kira-kira 55g",
                    "Port pengisian daya: Tipe-C",
                    "Impedansi speaker: 1602",
                ]),
        Product('Redmi Note 11 Pro 5G', 'Redmi Note 11 Pro 5G.png', 4099000,
                [
                    "Snapdragon® 695",
                    "CPU: CPU octa-core, hingga 2,2 GHz",
                    "GPU: Qualcomm® Adreno™ 619",
                    "LPDDR4X + UFS2.2",
                    "Tinggi: 164,19 mm",
                    "Lebar: 76,1 mm",
                    "Ketebalan: 8,12 mm",
                    "Berat: 202 g",
                    "DotDisplay AMOLED FHD+ 6,67",
                    "Refresh rate: Hingga 120 Hz",
                    "Kecerahan: HBM 700 nit (standar)",
                    "1200 nit kecerahan puncak (standar)",
                    "Rasio kontras: 4.500.0000:1",
                    "Resolusi: 2400 x 1080",
                    "Rentang warna luas DCI-P3",
                    "395 ppi",
                    "Sunlight display",
                ]),

        Product('Redmi Note 11 Pro', 'Redmi Note 11 Pro.png', 3699000,
                [
                    "MediaTek Helio G96",
                    "CPU: CPU octa-core, hingga 2,05GHz",
                    "GPU: ARM Mali-G57 MC2",
                    "6GB+128GB / 8GB+128GB",
                    "LPDDR4X + UFS2.2",
                    "Tinggi: 164,19 mm",
                    "Lebar: 76,1 mm",
                    "Ketebalan: 8,12 mm",
                    "Berat: 202 g",
                    "Layar 120Hz Super AMOLED",
                    "Refresh rate: Hingga 120Hz",
                    "Kecerahan: HBM 700 nit (typ),", 
                    "1200 nit kecerahan puncak (typ)",
                    "Rasio kontras: 4.500.0000:1",
                    "Resolusi: 2400 x 1080",
                    "Rentang warna luas DCI-P3",
                    "395 ppi",

                ]),
        Product('Redmi Note 11', 'Redmi Note 11.png', 2699000,
                [
                    "Snapdragon® 680",
                    "Proses manufaktur 6nm",
                    "CPU: CPU octa-core, hingga 2,4 GHz",
                    "GPU: GPU Qualcomm® Adreno™ 610",
                    "LPDDR4X + UFS2.2",
                    "Tinggi: 159,87 mm",
                    "Lebar: 73,87 mm",
                    "Ketebalan: 8,09 mm",
                    "Berat: 179 g",
                    "DotDisplay AMOLED FHD+ 6,43",
                    "Refresh rate: Hingga 90 Hz",
                    "Touch sampling rate: Hingga 180Hz",
                    "Kecerahan: HBM 700 nit (standar) ",
                    "1000 nit kecerahan puncak (standar)",
                    "Rasio kontras: 4.500.0000:1",
                    "Resolusi: 2400 x 1080",
                    "Rentang warna luas DCI-P3409 ppi",

                ]),
        Product('Redmi Note 12 Pro 5G', 'Redmi Note 12 Pro 5G.png', 4599000,
                [
                    "MediaTek Dimensity 1080",
                    "Proses manufaktur 6 nm",
                    "CPU: Octa-core CPU, hingga 2.6GHz", 
                    "GPU: Mali-G68",
                    "8GB+5GB* | 256GBLPDDR4X + UFS 2.2",
                    "Tinggi: 162.9mm",
                    "Lebar: 76mm",
                    "Ketebalan: 7.9mm",
                    "Berat: 187g",
                    "Layar 6.67 FHD+ P-OLED",
                    "Refresh rate: Hingga 120Hz",
                    "Kecerahan: ",
                    "kecerahan puncak 900 nits", 
                    "(typ)Rasio kontras: 5,000,000:1",
                    "Resolusi: 2400 x 1080Gamut ",
                    "warna lebar DCI-P3",
                    "Corning® Gorilla® Glass 5 protection",
                    "Mendukung Dolby Vision®",
                ]),
        Product('Redmi Note 12', 'Redmi Note 12.png', 2999000,
                [
                    "Snapdragon® 685",
                    "CPU: CPU octa-core, hingga 2,8 GHz",
                    "GPU: Adreno 610Proses manufaktur 6 nm",
                    "4 + 128/6 + 128/8 + 128 GBLPDDR4X + UFS 2.2",
                    "5.000 mAh",
                    "DotDisplay AMOLED 6,67",
                    "Bahan: E2 Pro",
                    "Refresh rate: 120 Hz",
                    "Touch sampling rate: Hingga 240 HzKecerahan: 450 nit (umum)",
                    "HBM 700 nit (umum)",
                    "kecerahan puncak 1.200 nit",
                    "Rasio kontras: 4.500.000:18 bit",
                    "Gamut warna DCI-P3 yang kaya",
                    "Resolusi: 2.400 x 1.080PPI 395Sunlight displayMode baca",
                ]),
        Product('Redmi Pad', 'Redmi Pad.png', 3499000,
                [
                    "Nama produk",
                    "Mi LCD Writing Tablet 13,5",
                    "Model produk",
                    "XMXHB02WC",
                    "Baterai",
                    "Sel kancing (CR2025)",
                    "Dimensi produk",
                    "318 mm x 225 mm x 7 mm 0,345 kg", 
                    "Berat netto",
                    "0,345 kg (termasuk baterai tipe",
                    "sel kancing)",
                    "Bahan utama",
                    "Lapisan film lembut LCD yang",
                    "terbuat dari polimer padat ABS",

                ]),
        Product('Redmi Watch 3', 'Redmi Watch 3.png', 1199000,
                [
                    "42.58 x 36.56 x 9.99mm",
                    "*Height, width and thickness dimensions exclude the strap and protrusions",
                    "37g (only watch body)",
                    "Black strap: TPU strap",
                    "size: 135 200mm",
                    "Ivory strap: Silicone strap",
                    "size: 135 200mm",
                    "Heart rate sensor (with blood oxygen sensor), accelerometer, gyroscope, geomagnetic sensor",
                    "Typical use time: 12 days Heavy use time: 7 days",
                    "Capacity: 289mAh",
                ]),
        Product('RedmiBook 15', 'RedmiBook 15.png', 7499000,
                [
                    "Tipe Layar: 15.6” FHD",
                    "Resolusi: 1920 x 1080",
                    "PPI: 141",
                    "Kontrol Kecerahan: Peredupan DC",
                    "Kecerahan: 220 nit (umum)",
                    "Rasio kontras: 500:1",
                    "Gamut warna: NTSC 45% (umum)",
                    "Sudut tampilan: 90°(H)",
                    "Windows 10 Home",
                    "11th Generation Intel® Core™ i3-1115G4 ",
                    "(up to 4.1 GHz, 2 Cores, 4 Threads, 6 MB Cache)", 
                    "11th Generation Intel® Core™ i5-11300H" ,
                    "(up to 4.4 GHz, 4 Cores, 8 Threads, 8 MB Cache)",
                    "Intel® UHD Graphics",
                    "Bluetooth 5.0",
                    "Wi-Fi 5 2.4Ghz/5GHz",
                ]),
        Product('Xiaomi 6A Type-A to Type-C Cable', 'Xiaomi 6A Type-A to Type-C Cable.png', 79000,
                [
                    "Nama produk",
                    "Kabel Tipe-A ke Tipe-C 6 A Xiaomi",
                    "Bahan",
                    "TPE",
                    "Port",
                    "USB-A ke Tipe-C",
                    "Warna",
                    "Putih",
                    "Perangkat yang kompatibel",
                    "Smartphone dan perangkat digital lain dengan port USB Tipe-C",
                    "Arus",
                    "6 A",
                    "Panjang",
                    "1 m",
                ]),
        Product('xiaomi 10t Pro', 'xiaomi 10t.png', 6999000,
                [
                    "Tinggi: 165,1 mm",
                    "Lebar: 76,4 mm",
                    "Ketebalan: 9,33 mm",
                    "Bobot: 218g (Mi 10T Pro), 216g (Mi 10T)",
                    "Qualcomm® Snapdragon™ 865 dengan 5G",
                    "Proses manufaktur efisien daya 7nmQualcomm® Kryo™ 585",
                    "CPU Octa-core, hingga 2,84 GHzQualcomm® ",
                    "Adreno™ 650 GPUModem X55 untuk konektivitas 5G secepat kilat",
                    "Resolusi: 2400 x 1080 FHD+",
                    "Mendukung Adaptive Sync dalam 30Hz/48Hz/50Hz/60Hz/90Hz/120 Hz/144 Hz",
                    "Bentang warna: NTSC 96% (typ), DCI-P3 98% (typ)",
                    "Tampilan True Color: JNCD≈0,39, Delta E≈0,63Mendukung MEMC",
                    "Mode Baca 3.0",
                ]),
        Product('xiaomi 11 T pro', 'xiaomi 11 T pro.png', 6199000,
                [
                    "Tinggi: 164,1 mm",
                    "Lebar: 76,9 mm",
                    "Ketebalan: 8,8 mm",
                    "Berat: 204 g",
                    "Qualcomm® Snapdragon™ 888",
                    "Proses pembuatan 5nm yang hemat daya",
                    "Kryo 680 CPU, hingga 2,84GHz, dengan teknologi ARM Cortex-X1",
                    "GPU: GPU Qualcomm® Adreno™ 660",
                    "AI: Mesin AI Generasi ke-6",
                    "Modem 5G Snapdragon X60",
                    "AMOLED 6,67” DotDisplay",
                    "2400 x 1080",
                    "Rasio aspek: 20:9",
                    "Dolby Vision® Support",
                    "Refresh rate: 120Hz",
                    "Touch sampling rate: hingga 480Hz",

                ]),

        Product('xiaomi 11 T', 'xiaomi 11 T.png', 4999000,
                [
                    "RAM & Penyimpanan",
                    "8GB+256GB",
                    "Penyimpanan RAM LPDDR4X + UFS 3.1",
                    "Dimensi",
                    "Tinggi: 164,1 mm",
                    "Lebar: 76,9 mm",
                    "Ketebalan: 8,8 mm",
                    "Berat: 203 g",
                    "Prosesor",
                    "Dimensity 1200-Ultra",
                    "Layar",
                    "AMOLED 6,67” DotDisplay",
                    "Resolusi: 2400 x 1080 FHD+",
                    "Rasio aspek: 20:9",
                    "Refresh rate: 120Hz",
                    "Touch sampling rate: hingga 480Hz",
                ]),
        Product('Xiaomi 22.5W Power Bank 10000mAh', 'Xiaomi 22.5W Power Bank 10000mAh.png', 4599000,
                [
                    "Nomor model:PB100LZM",
                    "Jenis baterai: Baterai polimer Lithium-ion",
                    "Daya baterai:37Wh 3,7V 10.000 mAh",
                    "Kapasitas maksim:5500 mAh (5.1V/2.6A)",
                    "Port input:Micro-USB/USB-C",
                    "Port output:2 x USB-A.",
                    "Parameter input:5V/2.1A",
                    "Parameter output:Output satu port 5, 1V/2,4A",
                    "Port output ganda 5.1V/2.6A",
                    "Dimensi produk: 150,5 x 73,6 x 15,1 mm",
                ]),
        Product('Xiaomi 67W Charging Combo (Type-A) EU', 'Xiaomi 67W Charging Combo (Type-A) EU.png', 299000,
                [
                    "Nama produk",
                    "Xiaomi 67W Charging Combo (Tipe-A)",
                    "Model produk",
                    "MDY-12-EH",
                    "Tipe port",
                    "USB-A untuk Tipe-C",
                    "Parameter input",
                    "100-240V~, 50/60Hz, 1,7A",
                    "Parameter output",
                    "5 V⎓3 A / 5-20 V⎓6,2-3,25 A (Maks. 67 W)",
                    "Dimensi",
                    "73x49.3x28mm (excludes pin length)",
                    "Suhu pengoperasian",
                    "-10℃~40℃",
                ]),
        Product('Xiaomi Air Purifier 4 Pro', 'Xiaomi Air Purifier 4 Pro.png', 3499000,
                [
                    "ModelAC-M15- SC Tingkat Penyaluran Udara Bersih Partikel",
                    "(Partikel CADR)500 m³/jam",
                    "Berat BersihSekitar 6,8 kg",
                    "Dimensi Item275x275x680 mm",
                    "Tingkat Kebisingan≤65 dB(A)",
                    "Area jangkauan efektif35-60㎡",
                ]),
        Product('Xiaomi Portable Electronic Air Compressor 1S', 'Xiaomi Portable Electronic Air Compressor 1S.png', 549000,
                [
                    "Nama Xiaomi Portable Electric Air Compressor 1S",
                    "ModelMJCQB05QJ",
                    "Standar yang diterapkan QXMQJ0002-2019",
                    "Dimensi124 x 71 x 45,3 mm",
                    "(Kompresor udara, tidak termasuk selang udara)",
                    "Kisaran tekanan pemompaan0,2-10,3 bar/3-150 psi",
                    "Suhu pengoperasianPengisian: 0℃—45℃. Pengosongan: -10℃—45℃",
                    "Suhu penyimpanan-10℃ hingga 45℃",
                    "Kapasitas baterai14,8 Wh",
                    "Nilai kebisingan selama pengoperasian<80 dB pada jarak 1 meter",
                    "Parameter input5V ⎓ 2A",

                ]),
        Product('Xiaomi Robot Vacuum E10', 'Xiaomi Robot Vacuum E10.png', 2499000,
                [
                    "Name Robotic Vacuum Cleaner",
                    "Model numberB112",
                    "Main unit dimensionsΦ325x80mm",
                    "Rated power35W",
                    "Rated voltage14.4V⎓",
                    "Charging voltage20V⎓",
                    "Battery capacity2500mAh (rated capacity)",
                    "2600mAh (nominal capacity)",
                    "Charging dock modelCDZB112",
                    "Rated input20V⎓ 0.6A",
                    "Rated output20V⎓ 0.6A",
                    "Product dimensions146x122x87.5mm",
                ]),
        Product('Xiaomi Smart Air Purifier 4 Lite', 'Xiaomi Smart Air Purifier 4 Lite.png', 1799000,
                [
                    "Nama produk",
                    "Xiaomi Smart Air Purifier 4 Lite",
                    "Model produk",
                    "AC-M17-SC",
                    "Dimensi produk",
                    "240 x 240 x 533,5 mm",
                    "Berat bersih produk",
                    "Sekitar 4,8 kg",
                    "Area jangkauan efektif",
                    "25-43 m²",
                    "Kebisingan",
                    "≤ 61dB(A)",
                    "PM CADR",
                    "360m³/jam",
                    "Efisiensi Purifikasi Partikel",
                    "Tinggi",
                ]),
        Product('Xiaomi smart band 7', 'Xiaomi smart band 7.png', 699000,
                [
                    "46,5 mm x 20,7 mm x 12,25 mm",
                    "Dimensi tinggi, lebar, dan ketebalan",
                    "Berat: 13,5 g",
                    "Ukuran: 160 mm-224 mm",
                    "Bahan: TPU",
                    "Gesper tali: aloi aluminium",
                    "Layar Sentuh AMOLED 1,62 inci",
                    "Resolusi: 192 x 490 piksel 326 PPI",
                    "Kecerahan: hingga 500 nit, dapat disesuaikan",
                    "Kaca antigores dengan lapisan anti-sidik jari",
                    "Tema layar: 100+",
                    "Jenis pengisian daya: pengisian daya secara magnetik",
                    "Waktu pengisian daya: ≤2 jam",

                ]),
        Product('Xiaomi Smart Camera C300', 'Xiaomi Smart Camera C300.png', 599000,
                [
                    "Nama produk",
                    "Xiaomi Smart Camera C300",
                    "No model produkXMC01",
                    "Dimensi Produk115 x 78 x 78mm",
                    "Kompatibel dengan",
                    "Android 4.4 atau iOS 9.0 dan keatas",
                    "Koneksi nirkabel",
                    "Wi-Fi IEEE 802.11b/g/n 2.4Ghz",
                    "Berat produk327g",
                    "Input daya5V=1A",
                    "ApertureF1.4",
                    "Resolusi2304 x 1296",
                    "Video encodingH.265",
                    "Penyimpanan",
                    "Kartu Micro SD (mendukung hingga 256GB)",
                ]),
        Product('Xiaomi TV Stick 4K', 'Xiaomi TV Stick 4K.png', 699000,
                [
                    "Output Resolution",
                    "4k",
                    "CPU",
                    "Quad-core Cortex-A35",
                    "GPU",
                    "Mali-G31 MP2",
                    "RAM",
                    "2GB",
                    "Storage",
                    "8GB",
                    "Operating System",
                    "Android TV™ 11",
                    "Content",
                    "Netflix, Amazon Prime Video and Youtube pre-installed",
                ]),
        Product('Xiaomi Watch S1 Active', 'Xiaomi Watch S1 Active.png', 1999000,
                [
                    "Sensor:Sensor detak jantung (dengan sensor saturasi oksigen)",
                    "akselerometer, giroskop, sensor geomagnetik, sensor atmosfer" ,
                    "sensor cahaya ambien",
                    "Dimensi:46,5 x 47,3 x 11 mm (tidak termasuk tali dan bagian pinggiranya)",
                    "Sistem penentuan posisi satelit:GPS, GLONASS, GALILEO, BDS, QZSS",
                    "Bingkai:Poliamida yang diperkuat serat kaca",
                    "Kapasitas baterai470 mAh",
                    "Layar:Layar AMOLED 1,43",
                    "Peringkat tahan air:5 ATM",
                    "Resolusi:466 x 466",
                    "Suhu pengoperasian:-10℃-45℃",
                    "Tali:TPU hitam dan biru, silikon putih",
                ]),
        Product('Xiaomi12', 'Xiaomi12.png', 6999000,
                [
                    "RAM & Kapasitas Penyimpanan",
                    "8GB+256GBRAM LPDDR5 + Media Penyimpanan UFS 3.1",
                    "Dimensi",
                    "Tinggi: 152,7 mmLebar: 69,9 mmKetebalan: 8,16 mmBerat: 180 g",
                    "Layar",
                    "DotDisplay Super AMOLED 6,28” FHD+",
                    "Prosesor",
                    "Snapdragon® 8 Gen 1",
                    "Kamera Belakang",
                    "50MP kamera wide",
                    "Baterai & Pengisian Daya",
                    "Baterai 4500mAh (typ)Pengisian daya turbo 67W", 
                    "dengan kabel Pengisian daya turbo 50W",
                    "nirkabel Reverse charging 10W",
                    "nirkabelPengisi daya 67W",
                    "disertakanUSB tipe CXiaomi AdaptiveCharge",
                ]),
        Product('xiaomi12lite5G', 'xiaomi12lite5G.png', 4799000,
                [
                    "Design",
                    "Matte finish",
                    "Dimension: 159.3 x 73.7 x 7.29mm",
                    "Weight: 173g",
                    "Display",
                    "6.55 FHD+ AMOLED DotDisplay",
                    "Rear camera",
                    "108MP wide-angle camera",
                    "8MP ultra-wide angle camera",
                    "2MP macro camera",
                    "Rear camera photography features",
                    "Rear camera video features",
                    "Rear video recording",
                    "Front camera",
                    "32MP in-display selfie camera",
                    "Processor",
                    "Snapdragon® 778G",

                ]),
        Product('xiaomi12pro', 'xiaomi12pro.png', 12199000,
                [
                    "Layar",
                    "WQHD+ DotDisplay AMOLED 6,73",
                    "Dimensi",
                    "Tinggi: 163,6mmLebar: 74,6mmKetebalan: 8,16mmBerat: 205g",
                    "Kamera Belakang",
                    "Rangkaian 50MP kamera tripel pro-grade",
                    "Kamera depan",
                    "Kamera depan 32 MP di sisi atas layar",
                    "Memori",
                    "12GB + 256GB",
                    "Prosesor",
                    "Snapdragon® 8 Gen 1",
                    "Baterai & Pengisian Daya",
                    "Baterai 4600 mAh (typ)120W Xiaomi HyperCharge ",
                    "Mode boost untuk pengisian daya hingga 100 Persen selama 18 menit",
                ]),
        Product('Mi 360 Home Security Camera 2K', 'Mi 360° Home Security Camera 2K.png', 599000,
                [
                    "Nama produkMi 360° Home Security Camera 2K",
                    "Berat bersih produk310 g",
                    "No. model produkMJSXJ09CM",
                    "Input daya5V=2A",
                    "Suhu pengoperasian-10°C hingga 50°C",
                    "AperturF1.4",
                    "Lens angle110°",
                    "Resolusi2304 x 1296",
                    "Dimensi produk115 x 78 x 78 mm",
                    "Video encodingH.265",
                    "Kompatibel denganAndroid 4.4 & iOS 9.0 atau lebih baru",
                    "PenyimpananKartu Micro SD (mendukung hingga 32 GB)",

                ]),
        Product('XIAOMI TV A2 55_', 'XIAOMI TV A2 55.jpg', 5899000,
                [
                    "Tipe Layar: UHD 4K",
                    "Resolusi: 3840 x 2160",
                    "Gamut warna: DCI-P3 90% (umum)",
                    "Kedalaman warna: 1,07 miliar",
                    "Refresh rate: 60 Hz",
                    "MEMC: hingga UHD 60 Hz",
                    "Sudut tampilan: 178°(H)/178°(V)",
                    "Mendukung Dolby Vision®, HDR10, HLG",
                    "Speaker (Output Suara): 2 x 12 W",
                    "Mendukung Dolby Audio™ dan DTS-HD®",
                    "Android TV™ 10",
                    "CPU: Quad A55",
                    "GPU: Mali G52 MP2",
                    "RAM: 2 GB",
                    "Penyimpanan: 16 GB",
                    "Netflix, Amazon Prime Video, dan YouTube bawaan",

                ]),
        Product('XIAOMI TV P1E 65_', 'XIAOMI TV P1E 65.jpg', 9399000,
                [
                    "Tipe Layar",
                    "UHD 4K",
                    "Resolusi",
                    "3840 x 2160",
                    "Gamut warna",
                    "DCI-P3 78% (standar)",
                    "Kedalaman warna",
                    "1,07 miliar (8-bit + FRC)",
                    "Refresh rate",
                    "60 Hz",
                    "MEMC",
                    "UHD 60 Hz",
                    "Sudut tampilan",
                    "178°(H)/178°(V)",
                    "Mendukung HDR10, HLG, Dolby Vision®",
                ]),
            ]

    app = KumpulanProduk(products)
    app.mainloop()
