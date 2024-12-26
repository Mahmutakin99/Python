'''
from math import *
print("************************************\n\tHesap makinesi programı\n************************************\n      çıkmak için 'q'ya basınız...")
while True:
    secim=input("************************************\n1)toplama\n2)cıkarma\n3)carpma\n4)bölme\n5)yuzde alma\n6)üs alma\n7)karekok alma\n8)on tabanlı logaritma\n9)Ebob/Ekok\nyapmak istediğiniz işlemi seciniz:\n************************************\n")
    print("seçilen işlem kodu: ",secim)
    if(secim=='q'):
        print("programdan çıkılıyor...")
        break
    elif(secim=='1'):
        print("Yapacağınız işlem (toplama)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a+b}")
    elif(secim=='2'):
        print("Yapacağınız işlem (çıkarma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a-b}")
    elif(secim=='3'):
        print("Yapacağınız işlem (çarpma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a*b}")
    elif(secim=='4'):
        print("Yapacağınız (işlem bölme)dir:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a/b}")
    elif(secim=='5'):
        print("Yapacağınız işlem (yüzde alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("Yüzde kaç almak istersiniz:"))
        print(f"************************************\nsonuç: {(a*b)/100}")
    elif(secim=='6'):
        print("Yapacağınız işlem (üs alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=int(input("Üs giriniz:"))
        print(f"************************************\nsonuç: {a**b}")
    elif(secim=='7'):
        print("Yapacağınız işlem (karekök alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a**(0.5)}")
    elif(secim=='8'):
        print("Yapacağınız işlem (on tabanlı logaritma alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        print(f"************************************\nsonuç: {log10(a)}")
    elif(secim=='9'):
        print("Yapacağınız işlem (Ebob/Ekok Alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        ebob= ebob(a,b)
        ekok= ekok(a,b)
        print(f"************************************\nEbob: {ebob}\tEkok: {ekok}")
    else:
        print("seçilen işlem kodu hatalıdır:")  

'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QInputDialog
from math import log10, sqrt, gcd
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(100, 100, 400, 300)

        # Vertical layout
        vbox = QVBoxLayout()

        # Result screen
        self.result = QLineEdit(self)
        self.result.setPlaceholderText("Sonuç Ekranı")
        vbox.addWidget(self.result)

        # Horizontal layout for buttons
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()

        # Creating buttons
        btn_add = QPushButton('Toplama', self)
        btn_subtract = QPushButton('Çıkarma', self)
        btn_multiply = QPushButton('Çarpma', self)
        btn_divide = QPushButton('Bölme', self)
        btn_percentage = QPushButton('Yüzde', self)
        btn_power = QPushButton('Üs', self)
        btn_sqrt = QPushButton('Karekök', self)
        btn_log = QPushButton('Log10', self)
        btn_gcd_lcm = QPushButton('Ebob/Ekok', self)
        btn_exit = QPushButton('Çıkış', self)

        # Connecting buttons to functions
        btn_add.clicked.connect(self.add)
        btn_subtract.clicked.connect(self.subtract)
        btn_multiply.clicked.connect(self.multiply)
        btn_divide.clicked.connect(self.divide)
        btn_percentage.clicked.connect(self.percentage)
        btn_power.clicked.connect(self.power)
        btn_sqrt.clicked.connect(self.sqrt)
        btn_log.clicked.connect(self.log)
        btn_gcd_lcm.clicked.connect(self.gcd_lcm)
        btn_exit.clicked.connect(self.close)

        # Adding buttons to horizontal layouts
        hbox1.addWidget(btn_add)
        hbox1.addWidget(btn_subtract)
        hbox2.addWidget(btn_multiply)
        hbox2.addWidget(btn_divide)
        hbox3.addWidget(btn_percentage)
        hbox3.addWidget(btn_power)
        hbox4.addWidget(btn_sqrt)
        hbox4.addWidget(btn_log)
        hbox5.addWidget(btn_gcd_lcm)
        hbox6.addWidget(btn_exit)

        # Adding horizontal layouts to vertical layout
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)

        # Setting the layout of the main window
        self.setLayout(vbox)

    def get_two_inputs(self):
        text1, ok1 = QInputDialog.getDouble(self, 'Input', 'Birinci sayıyı giriniz:')
        text2, ok2 = QInputDialog.getDouble(self, 'Input', 'İkinci sayıyı giriniz:')
        if ok1 and ok2:
            return text1, text2
        else:
            self.result.setText("Hata: Geçersiz giriş")
            return None, None

    def get_one_input(self):
        text, ok = QInputDialog.getDouble(self, 'Input', 'Bir sayı giriniz:')
        if ok:
            return text
        else:
            self.result.setText("Hata: Geçersiz giriş")
            return None

    def add(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            self.result.setText(str(a + b))

    def subtract(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            self.result.setText(str(a - b))

    def multiply(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            self.result.setText(str(a * b))

    def divide(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            try:
                self.result.setText(str(a / b))
            except ZeroDivisionError:
                self.result.setText("Hata: Bölme işleminde sıfır kullanılamaz.")

    def percentage(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            self.result.setText(str((a * b) / 100))

    def power(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            self.result.setText(str(a ** b))

    def sqrt(self):
        a = self.get_one_input()
        if a is not None:
            self.result.setText(str(sqrt(a)))

    def log(self):
        a = self.get_one_input()
        if a is not None:
            self.result.setText(str(log10(a)))

    def gcd_lcm(self):
        a, b = self.get_two_inputs()
        if a is not None and b is not None:
            ebob = gcd(int(a), int(b))
            ekok = (a * b) / ebob
            self.result.setText(f"Ebob: {ebob} Ekok: {ekok}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

