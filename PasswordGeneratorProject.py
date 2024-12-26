# from random import * 
# from time import *
# while True:

#     letters=[] 
    
#     # Instead of typing repeatedly in different languages, use this list to copy the characters of the desired language into this list and use it
#     eng_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
#     tr_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z',
#                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
    
#     ger_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#                  'ä', 'ö', 'ü', 'ß','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
#                  'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'ẞ']
    
#     fr_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#              'à', 'â', 'ç', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü', 'ÿ', 'À', 'Â', 'Ç', 'É', 'È', 'Ê', 'Ë', 'Î', 'Ï', 'Ô', 'Ù', 'Û', 'Ü', 'Ÿ']
    
#     ru_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
#                   'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
#                   'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    
#     ko_letters = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ',
#              'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ']
    
#     ja_letters = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の',
#              'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ','ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 
#              'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ',]




#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



#     password_list=[] # This empty list is used to hold the characters the user wants.
    
#     select=int(input('''**********************************\n1 to start/continue processing
# Press 0 to stop/finish.
# Process selection: '''))
#     if(select==0):
#         select2=str(input("you have chosen to stop the transaction, should the transaction be executed? 'yes' or 'no' "))
#         if(select2=='yes'):
#             break
#         elif(select2=='no'):
#             continue
#         else:
#             print("you logged in incorrectly please correct")
#             continue
#     if (select > 1 or select < 0):
#         print("Please enter the correct code for selection.")
#         continue
#     while True:    
#         print("In which language do you use the keyboard? ")
#         print("1) English\n2) Turkish\n3) German\n4) French\n5) Russian\n6) Korean\n7) Japanese")
#         lang_select=int(input("\n--> "))

#         if lang_select == 1:
#             letters=[i for i in eng_letters]
#         elif lang_select == 2:
#             letters=[i for i in tr_letters]
#         elif lang_select == 3:
#             letters=[i for i in ger_letters]
#         elif lang_select == 4:
#             letters=[i for i in fr_letters]
#         elif lang_select == 5:
#             letters=[i for i in ru_letters]
#         elif lang_select == 6:
#             letters=[i for i in ko_letters]
#         elif lang_select == 7:
#             letters=[i for i in ja_letters]
#         else:
#             print("You have entered an incorrect selection code, please correct it.")
#             continue

#         # Simple random password generation 
#         nr_letters= int(input("How many characters will be in the password to be created: ")) 
#         if(nr_letters > 0):
#             for char in range(0, nr_letters): 
#                 password_list.append(choice(letters))
#         elif(nr_letters <= 0):
#             print("A password will be created without characters.")
            
#         nr_numbers = int(input("How many numeric characters will be in the password to be created: ")) 
#         if(nr_numbers > 0):
#             for _ in range(0, nr_numbers): 
#                 password_list.append(choice(numbers)) 
#         elif(nr_numbers <= 0):
#             print("A password will be created without numeric characters.")

#         nr_symbols = int(input("How many symbols will be in the password to be created: ")) 
#         if(nr_symbols > 0):
#             for _ in range(0, nr_symbols): 
#                 password_list.append(choice(symbols))
#         elif(nr_symbols <= 0):
#             print("A password will be generated without a symbol.") 
            
#         # Create an empty password variable
#         password =""

#         # Sort randomly selected characters randomly within the list without returning a new list
#         shuffle(password_list) 

#         # Assign the characters in the list to the created password variable
#         for char in password_list: 
#             password += char 

#         # Print randomly generated password on screen
#         if(nr_symbols == 0 and nr_letters == 0 and nr_numbers == 0):
#             print("A minimum number of valid characters must be entered to create a password.")
#         else:
#             print(f"Your unique password generated: {password}")
#         break

'''
import tkinter as tk
from tkinter import ttk
from random import choice, shuffle

# Fonksiyonlar
def generate_password():
    letters = []
    eng_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tr_letters = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    ger_letters = 'abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜẞ'
    fr_letters = 'abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüÿABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÇÉÈÊËÎÏÔÙÛÜŸ'
    ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ko_letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ'
    ja_letters = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんガギグゲゴザジズゼゾダヂヅデドバビブベボパ'

    numbers = '0123456789'
    symbols = '!#$%&()*+'

    lang = lang_var.get()
    if lang == 'English':
        letters = eng_letters
    elif lang == 'Turkish':
        letters = tr_letters
    elif lang == 'German':
        letters = ger_letters
    elif lang == 'French':
        letters = fr_letters
    elif lang == 'Russian':
        letters = ru_letters
    elif lang == 'Korean':
        letters = ko_letters
    elif lang == 'Japanese':
        letters = ja_letters

    password_list = []

    try:
        nr_letters = int(letters_var.get())
        nr_numbers = int(numbers_var.get())
        nr_symbols = int(symbols_var.get())

        for _ in range(nr_letters):
            password_list.append(choice(letters))
        for _ in range(nr_numbers):
            password_list.append(choice(numbers))
        for _ in range(nr_symbols):
            password_list.append(choice(symbols))

        shuffle(password_list)

        password = ''.join(password_list)
        result_var.set(password)
    except ValueError:
        result_var.set("Invalid input! Please enter numbers only.")

# Arayüz
root = tk.Tk()
root.title("Şifre Oluşturucu")

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dil seçimi
ttk.Label(mainframe, text="Klavye dili:").grid(column=1, row=1, sticky=tk.W)
lang_var = tk.StringVar()
lang_combobox = ttk.Combobox(mainframe, textvariable=lang_var)
lang_combobox['values'] = ('English', 'Turkish', 'German', 'French', 'Russian', 'Korean', 'Japanese')
lang_combobox.grid(column=2, row=1, sticky=(tk.W, tk.E))

# Harf sayısı
ttk.Label(mainframe, text="Harf sayısı:").grid(column=1, row=2, sticky=tk.W)
letters_var = tk.StringVar()
ttk.Entry(mainframe, textvariable=letters_var).grid(column=2, row=2, sticky=(tk.W, tk.E))

# Rakam sayısı
ttk.Label(mainframe, text="Rakam sayısı:").grid(column=1, row=3, sticky=tk.W)
numbers_var = tk.StringVar()
ttk.Entry(mainframe, textvariable=numbers_var).grid(column=2, row=3, sticky=(tk.W, tk.E))

# Sembol sayısı
ttk.Label(mainframe, text="Sembol sayısı:").grid(column=1, row=4, sticky=tk.W)
symbols_var = tk.StringVar()
ttk.Entry(mainframe, textvariable=symbols_var).grid(column=2, row=4, sticky=(tk.W, tk.E))

# Sonuç
ttk.Label(mainframe, text="Oluşturulan şifre:").grid(column=1, row=5, sticky=tk.W)
result_var = tk.StringVar()
ttk.Entry(mainframe, textvariable=result_var, state='readonly').grid(column=2, row=5, sticky=(tk.W, tk.E))

# Buton
ttk.Button(mainframe, text="Şifre Oluştur", command=generate_password).grid(column=2, row=6, sticky=tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
'''







import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from random import choice, shuffle

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Şifre Oluşturucu')

        # Dil seçimi
        self.lang_label = QLabel('Klavye dili:')
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(['English', 'Turkish', 'German', 'French', 'Russian', 'Korean', 'Japanese'])

        # Harf sayısı
        self.letters_label = QLabel('Harf sayısı:')
        self.letters_input = QLineEdit()

        # Rakam sayısı
        self.numbers_label = QLabel('Rakam sayısı:')
        self.numbers_input = QLineEdit()

        # Sembol sayısı
        self.symbols_label = QLabel('Sembol sayısı:')
        self.symbols_input = QLineEdit()

        # Sonuç
        self.result_label = QLabel('Oluşturulan şifre:')
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)

        # Butonlar
        self.generate_button = QPushButton('Şifre Oluştur')
        self.generate_button.clicked.connect(self.generate_password)

        self.exit_button = QPushButton('Çıkış')
        self.exit_button.clicked.connect(self.close_application)

        # Layout
        vbox = QVBoxLayout()

        lang_layout = QHBoxLayout()
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.lang_combo)

        letters_layout = QHBoxLayout()
        letters_layout.addWidget(self.letters_label)
        letters_layout.addWidget(self.letters_input)

        numbers_layout = QHBoxLayout()
        numbers_layout.addWidget(self.numbers_label)
        numbers_layout.addWidget(self.numbers_input)

        symbols_layout = QHBoxLayout()
        symbols_layout.addWidget(self.symbols_label)
        symbols_layout.addWidget(self.symbols_input)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_display)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.generate_button)
        buttons_layout.addWidget(self.exit_button)

        vbox.addLayout(lang_layout)
        vbox.addLayout(letters_layout)
        vbox.addLayout(numbers_layout)
        vbox.addLayout(symbols_layout)
        vbox.addLayout(result_layout)
        vbox.addLayout(buttons_layout)

        self.setLayout(vbox)

    def generate_password(self):
        eng_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tr_letters = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
        ger_letters = 'abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜẞ'
        fr_letters = 'abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüÿABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÇÉÈËÎÏÔÙÛÜŸ'
        ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        ko_letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ'
        ja_letters = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんガギグゲゴザジズゼゾダヂヅデドバビブベボパ'

        numbers = '0123456789'
        symbols = '!#$%&()*+'

        letters = ''
        lang = self.lang_combo.currentText()
        if lang == 'English':
            letters = eng_letters
        elif lang == 'Turkish':
            letters = tr_letters
        elif lang == 'German':
            letters = ger_letters
        elif lang == 'French':
            letters = fr_letters
        elif lang == 'Russian':
            letters = ru_letters
        elif lang == 'Korean':
            letters = ko_letters
        elif lang == 'Japanese':
            letters = ja_letters

        password_list = []

        try:
            nr_letters = int(self.letters_input.text())
            nr_numbers = int(self.numbers_input.text())
            nr_symbols = int(self.symbols_input.text())

            for _ in range(nr_letters):
                password_list.append(choice(letters))
            for _ in range(nr_numbers):
                password_list.append(choice(numbers))
            for _ in range(nr_symbols):
                password_list.append(choice(symbols))

            shuffle(password_list)

            password = ''.join(password_list)
            self.result_display.setText(password)
        except ValueError:
            QMessageBox.warning(self, 'Hata', 'Lütfen geçerli sayılar girin!')

    def close_application(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())

