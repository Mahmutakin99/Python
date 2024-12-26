# def VKI():
#     from math import pow
#     kilo = float(input("Kilogram cinsinden kilonuzu Giriniz : "))
#     boy = float(input("cm cinsinden boyunuzu giriniz : "))

#     vki = kilo / pow(boy / 100, 2)
#     print("Vücut Kitle İndeksiniz: {:.2f}".format(vki))
#     # : Biçimlendirme dizesinin başlangıcını belirtir.
#     # . Ondalık ayırıcıyı belirtir.
#     # 2 İki ondalık basamak gösterileceğini belirtir.
#     # f İfade float (ondalıklı sayı) türünde olduğunu belirtir.
#     # round fonksiyonuda kullanılabilir #
#     print("Durumunuz: ", end="")

#     if vki <= 18.5:
#         print("Zayıf")
#         print("{:.2f} kg kilo Almanız Gerekiyor".format(18.5 * pow(boy / 100, 2) - kilo))
#     elif vki <= 24.9:
#         print("Normal")
#         print("Kilo almaya veya vermeye ihtiyacınız yok.")
#     elif vki <= 29.9:
#         print("Fazla Kilolu")
#         print("{:.2f} kg kilo Vermeniz Gerekiyor".format(kilo - 24.9 * pow(boy / 100, 2)))
#     elif vki <= 39.9:
#         print("Obez")
#         print("{:.2f} kg kilo Vermeniz Gerekiyor".format(kilo - 24.9 * pow(boy / 100, 2)))
# if __name__ == "__main__":
#     VKI()


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys
from math import pow

def calculate_vki(kilo, boy):
    vki = kilo / pow(boy / 100, 2)
    if vki <= 18.5:
        durum = "Zayıf"
        ideal_kilo = 18.5 * pow(boy / 100, 2)
        fark = ideal_kilo - kilo
        kilo_durum = "{:.2f} kg kilo almanız gerekiyor.".format(fark)
    elif vki <= 24.9:
        durum = "Normal"
        kilo_durum = "Kilo almaya veya vermeye ihtiyacınız yok."
    elif vki <= 29.9:
        durum = "Fazla Kilolu"
        ideal_kilo = 24.9 * pow(boy / 100, 2)
        fark = kilo - ideal_kilo
        kilo_durum = "{:.2f} kg kilo vermeniz gerekiyor.".format(fark)
    elif vki <= 39.9:
        durum = "Obez"
        ideal_kilo = 24.9 * pow(boy / 100, 2)
        fark = kilo - ideal_kilo
        kilo_durum = "{:.2f} kg kilo vermeniz gerekiyor.".format(fark)
    else:
        durum = "Ciddi Obez"
        ideal_kilo = 24.9 * pow(boy / 100, 2)
        fark = kilo - ideal_kilo
        kilo_durum = "{:.2f} kg kilo vermeniz gerekiyor.".format(fark)

    return vki, durum, kilo_durum

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Vücut Kitle İndeksi Hesaplama")
        self.setGeometry(200, 200, 400, 300)

        self.initUI()

    def initUI(self):
        self.label1 = QLabel(self)
        self.label1.setText("Kilonuzu giriniz: ")
        self.label1.move(20, 30)
        
        self.kilo_input = QLineEdit(self)
        self.kilo_input.setGeometry(200, 30, 150, 20)
        
        self.label2 = QLabel(self)
        self.label2.setText("Boyunuzu giriniz: ")
        self.label2.move(20, 70)
        
        self.boy_input = QLineEdit(self)
        self.boy_input.setGeometry(200, 70, 150, 20)

        self.button = QPushButton(self)
        self.button.setText("Hesapla")
        self.button.setGeometry(150, 120, 100, 30)
        self.button.clicked.connect(self.calculate)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(20, 170, 360, 100)
        self.result_label.setWordWrap(True)

    def calculate(self):
        kilo = float(self.kilo_input.text())
        boy = float(self.boy_input.text())
        vki, durum, kilo_durum = calculate_vki(kilo, boy)

        result_text = "Vücut Kitle İndeksiniz: {:.2f}\nDurumunuz: {}\n{}".format(vki, durum, kilo_durum)
        self.result_label.setText(result_text)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
