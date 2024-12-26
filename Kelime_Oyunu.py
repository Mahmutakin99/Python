# from random import choice
# from Kelimeler import sozluk

# kelime_listesi = sozluk

# def kelime_oyunu():
#     yanlis_tahminler = []
#     puan = 0

#     def yeni_kelime():
#         kelime = choice(list(kelime_listesi.keys()))
#         anlam = kelime_listesi[kelime]
#         return kelime, anlam
    
#     def kelime_goster(kelime):
#         print(f"\nKelime: {kelime}")
    
#     def kelime_kontrol(kelime, anlam, tahmin):
#         if tahmin.lower() == anlam.lower():
#             nonlocal puan
#             puan += 10
#             print("Doğru tahmin!")
#             print(f"Şu anki puanınız: {puan}")
#             return True
#         else:
#             print(f"Yanlış! Doğru cevap: {anlam}")
#             return False
    
#     def oyun_bitti_mi():
#         print(f"\nOyun Bitti! Toplam Puanınız: {puan}")
#         if yanlis_tahminler:
#             print("\nYanlış Tahmin Edilen Kelimeler ve Anlamları:")
#             for kelime, anlam in yanlis_tahminler:
#                 print(f"- {kelime}: {anlam}")
#         else:
#             print("\nTüm tahminler doğru")

#     print("Kelime Oyunu")
#     print("Geçmek için 'geç', Çıkmak için 'çıkış' yazınız.")

#     while True:
#         kelime, anlam = yeni_kelime()
#         kelime_goster(kelime)
        
#         tahmin = input("\nBu kelimenin anlamı nedir? (Tahmininizi giriniz): ")
        
#         if tahmin.lower() == 'çıkış':
#             oyun_bitti_mi()
#             break
#         elif tahmin.lower() == 'geç':
#             yanlis_tahminler.append((kelime, anlam))
#             print(f"Kelimeyi geçtiniz. Doğru cevap: {anlam}")
#             continue
#         elif not kelime_kontrol(kelime, anlam, tahmin):
#             yanlis_tahminler.append((kelime, anlam))

# kelime_oyunu()





import time
from random import choice
from Kelimeler import sozluk

kelime_listesi = sozluk

def kelime_oyunu():
    yanlis_tahminler = []
    puan = 0
    tahmin_hakki = 0
    zorluk = ""

    def yeni_kelime():
        kelime = choice(list(kelime_listesi.keys()))
        anlam = kelime_listesi[kelime]
        return kelime, anlam
    
    def kelime_goster(kelime):
        print(f"\nKelime: {kelime}")
    
    def kelime_kontrol(anlam, tahmin):
        if tahmin.lower() == anlam.lower():
            nonlocal puan
            if zorluk == 'kolay':
                puan += 5
            else:
                puan += 20
            print("Doğru tahmin!")
            print(f"Şu anki puanınız: {puan}")
            return True
        else:
            print(f"Yanlış! Doğru cevap: {anlam}")
            return False
    
    def oyun_bitti_mi():
        print(f"\nOyun Bitti! Toplam Puanınız: {puan}")
        if yanlis_tahminler:
            print("\nYanlış Tahmin Edilen Kelimeler ve Anlamları:")
            for kelime, anlam in yanlis_tahminler:
                print(f"- {kelime}: {anlam}")
        else:
            print("\nTüm tahminler doğru")

    def zamanli_tahmin():
        start_time = time.time()
        try:
            tahmin = input("\nBu kelimenin anlamı nedir? (Tahmininizi giriniz): ")
            if time.time() - start_time > 10:  # 10 saniye zaman sınırı
                print("Zaman doldu! Kelimeyi geçtiniz.")
                return 'geç'
            return tahmin
        except:
            return 'geç'

    def zorluk_seviyesi():
        print("Zorluk seviyesini seçiniz: (Kolay: sınırsız tahmin, Zor: 3 tahmin hakkı)")
        nonlocal zorluk, tahmin_hakki
        while zorluk not in ['kolay', 'zor']:
            zorluk = input("Kolay veya zor seçiniz: ").lower()
        
        if zorluk == 'kolay':
            tahmin_hakki = float('inf')  # Sınırsız tahmin
        else:
            tahmin_hakki = 3  # 3 tahmin hakkı

    print("Kelime Oyunu")
    print("Geçmek için 'geç', Çıkmak için 'çıkış' yazınız.")
    zorluk_seviyesi()

    while True:
        kelime, anlam = yeni_kelime()
        kelime_goster(kelime)
        
        tahmin_sayisi = 0
        while tahmin_sayisi < tahmin_hakki:
            tahmin = zamanli_tahmin()
            
            if tahmin.lower() == 'çıkış':
                oyun_bitti_mi()
                return
            elif tahmin.lower() == 'geç':
                yanlis_tahminler.append((kelime, anlam))
                print(f"Kelimeyi geçtiniz. Doğru cevap: {anlam}")
                break  # Yeni kelimeye geç
            elif not kelime_kontrol(anlam, tahmin):
                tahmin_sayisi += 1
                yanlis_tahminler.append((kelime, anlam))
                break  # Yanlış tahminde yeni kelimeye geç
            else:
                break  # Doğru tahmin yapıldıysa yeni kelimeye geç

kelime_oyunu()







# import Kelimeler
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
# from PyQt5.QtCore import Qt
# from random import choice
# import sys

# # Örnek sözlük yapıları
# A1_sözlük = Kelimeler.A1_sözlük
# A2_sözlük = Kelimeler.A2_sözlük
# B1_sözlük = Kelimeler.B1_sözlük
# B2_sözlük = Kelimeler.B2_sözlük

# # Ana pencere sınıfı
# class KelimeOyunuPenceresi(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
        
#     def initUI(self):
#         self.setWindowTitle('Kelime Oyunu')
#         self.setGeometry(100, 100, 600, 400)
        
#         # Ana widget ve layout
#         self.centralWidget = QWidget()
#         self.layout = QVBoxLayout(self.centralWidget)
        
#         # Seviye seçimi için combo box
#         self.seviyeLabel = QLabel("Seviye Seçiniz:")
#         self.layout.addWidget(self.seviyeLabel)
        
#         self.seviyeComboBox = QComboBox()
#         self.seviyeComboBox.addItems(["A1", "A2", "B1", "B2"])
#         self.layout.addWidget(self.seviyeComboBox)
        
#         # Kelime ve tahmin gösterimi
#         self.kelimeLabel = QLabel("Kelime: ")
#         self.layout.addWidget(self.kelimeLabel)
        
#         self.tahminInput = QLineEdit()
#         self.layout.addWidget(self.tahminInput)
        
#         # Tahmin butonu
#         self.tahminButton = QPushButton("Tahmin Et")
#         self.tahminButton.clicked.connect(self.tahminEt)
#         self.layout.addWidget(self.tahminButton)

#         # Geç butonu
#         self.gecButton = QPushButton("Geç")
#         self.gecButton.clicked.connect(self.gec)
#         self.layout.addWidget(self.gecButton)
        
#         # Çıkış butonu
#         self.cikisButton = QPushButton("Çıkış")
#         self.cikisButton.clicked.connect(self.cikis)
#         self.layout.addWidget(self.cikisButton)
        
#         # Sonuç gösterimi
#         self.sonucLabel = QLabel("")
#         self.layout.addWidget(self.sonucLabel)
        
#         # Puan gösterimi
#         self.puanLabel = QLabel("Puan: 0")
#         self.layout.addWidget(self.puanLabel)
        
#         # Oyun başlatma butonu
#         self.baslatButton = QPushButton("Oyunu Başlat")
#         self.baslatButton.clicked.connect(self.oyunuBaslat)
#         self.layout.addWidget(self.baslatButton)
        
#         self.setCentralWidget(self.centralWidget)
#         self.puan = 0
#         self.yanlis_tahminler = []
#         self.gecilen_kelime = []
#         self.kelime_listesi = {}
#         self.current_kelime = ""
#         self.current_anlam = ""
    
#     def oyunuBaslat(self):
#         seviye = self.seviyeComboBox.currentText()
#         if seviye == "A1":
#             self.kelime_listesi = A1_sözlük
#         elif seviye == "A2":
#             self.kelime_listesi = A2_sözlük
#         elif seviye == "B1":
#             self.kelime_listesi = B1_sözlük
#         elif seviye == "B2":
#             self.kelime_listesi = B2_sözlük
        
#         self.yeniKelime()
    
#     def yeniKelime(self):
#         self.current_kelime, self.current_anlam = self.kelimeSec()
#         self.kelimeLabel.setText(f"Kelime: {self.current_kelime}")
#         self.tahminInput.clear()
#         self.sonucLabel.setText("")
    
#     def kelimeSec(self):
#         kelime = choice(list(self.kelime_listesi.keys()))
#         anlam = self.kelime_listesi[kelime]
#         return kelime, anlam
    
#     def tahminEt(self):
#         tahmin = self.tahminInput.text()
#         if tahmin.lower() == self.current_anlam.lower():
#             self.puan += 10
#             self.sonucLabel.setText("Doğru tahmin!")
#         else:
#             self.sonucLabel.setText(f"Yanlış! Doğru cevap: {self.current_anlam}")
#             self.yanlis_tahminler.append((self.current_kelime, self.current_anlam))
        
#         self.puanLabel.setText(f"Puan: {self.puan}")
#         self.yeniKelime()
    
#     def gec(self):
#         self.gecilen_kelime.append((self.current_kelime, self.current_anlam))
#         self.sonucLabel.setText(f"Geçildi! Doğru cevap: {self.current_anlam}")
#         self.yeniKelime()
    
#     def cikis(self):
#         cikis_mesaji = f"Toplam Puanınız: {self.puan}\n"
#         if self.yanlis_tahminler:
#             cikis_mesaji += "\nYanlış Tahmin Edilen Kelimeler ve Anlamları:\n"
#             for kelime, anlam in self.yanlis_tahminler:
#                 cikis_mesaji += f"- {kelime}: {anlam}\n"
#         if self.gecilen_kelime:
#             cikis_mesaji += "\nGeçilen Kelimeler ve Anlamları:\n"
#             for kelime, anlam in self.gecilen_kelime:
#                 cikis_mesaji += f"- {kelime}: {anlam}\n"
        
#         QMessageBox.information(self, "Oyun Bitti", cikis_mesaji)
#         self.close()

# # Uygulama başlatma
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     pencere = KelimeOyunuPenceresi()
#     pencere.show()
#     sys.exit(app.exec_())