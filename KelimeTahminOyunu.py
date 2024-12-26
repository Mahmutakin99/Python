'''
from random import choice

# We create a bool value to terminate the outermost loop if the user wants to exit the application.
Accuracy = False

while True:
  if Accuracy == True:
    # If the user guessed the word correctly, we ask if they want to quit the game.
      choice = input("You guessed the word correctly, do you want to start a new game (yes or no):\n--> ").lower()
      if choice == 'yes':
          Accuracy = False
          continue
      elif choice == 'no':
          break
      else:
        # we take precautions in case the user enters something wrong.
          print("incorrect entry exiting the program")
          continue
    
  # We create a list of words. you can add the words you want and remove the words you don't want.
  Words=['GalataSaray', 'Book', 'Wind', 'Pen', 'Flower', 'Computer', 'Sea', 'Cat', 'Tree', 'Star',
 'Music', 'Mountain', 'Clock', 'Coffee', 'Table', 'Chair', 'Phone', 'Picture', 'Hat', 'Apple',
 'Glass', 'Plate', 'Television', 'Bag', 'Shoe', 'Pants', 'Jacket', 'Glasses', 'Lamp',
 'Map', 'Building', 'Bridge', 'Train', 'Car', 'Bicycle', 'Plane', 'Balloon', 'House', 'Street', 'Park',
 'Garden', 'Child', 'Baby', 'Rain', 'Snow', 'Sun', 'Sand', 'Cloud', 'Bird', 'Fish', 'Lake', 'River',
 'Forest', 'Island', 'Lighthouse', 'Route', 'Bus', 'Calendar', 'Notebook', 'Pencil case', 'Eraser', 'Paint', 'Brush',
 'Canvas', 'Kitchen', 'Bathroom', 'Bed', 'Room', 'Living room', 'Corridor', 'Frame', 'Lock', 'Key', 'Fruit',
 'Vegetable', 'Chocolate', 'Ice cream', 'Cake', 'Bread', 'Cheese', 'Olive', 'Tomato', 'Cucumber', 'Pepper',
 'Potato', 'Carrot', 'Onion', 'Garlic', 'Parsley', 'Dill', 'Mint', 'Lemon', 'Orange', 'Tangerine',
 'Watermelon', 'Melon', 'Cherry', 'Strawberry', 'Banana', 'Grape', 'Apple', 'Pear']

  # We select a random word from our list of words using the choice function from the random module, which allows us to choose randomly.
  Word = choice(Words).lower()
  # We create a list of characters consisting of '_' of the length of our randomly chosen word.
  Prediction = []
  for _ in range(len(Word)):
      Prediction.append('_')
      # or
      # Prediction += '_'
  while True:
    print(Prediction)
    # We ask the user to guess the word by taking a letter
    inp1=input("Enter a letter, write a prediction to guess:\n--> ").lower()
    # we ask the user if he/she has a guess, if so, we ask him/her to enter a guess, 
    # if correct, the guess is correct, if incorrect, the guess is incorrect, we tell him/her to enter a guess or letter again
    if inp1 == 'prediction':
      inp2 = input("enter your prediction:\n--> ").lower()
      if inp2 == Word:
        print(f"Congratulations, our word: {Word}")
        Accuracy = True
        break
      else:
        print("Wrong prediction, try again")
        continue
    
    # If the entered letter is in our word, we replace the '_' character with the letter in the appropriate order in the prediction list.
    i = 0
    for letter in Word:
      if letter == inp1:
        Prediction[i] = letter
      i += 1
    
    #we check if there are any '_' characters left in the guess list because the word must be guessed to end the game
    x = 0
    for Character in Prediction:
      if Character == '_':
        x += 1
    if x == 0:
      print(Prediction)
      Accuracy = True
      break


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont
from random import choice

class WordGuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kelime Tahmin Oyunu')
        self.setGeometry(100, 100, 500, 300)

        self.words = [
            'GalataSaray', 'Book', 'Wind', 'Pen', 'Flower', 'Computer', 'Sea', 'Cat', 'Tree', 'Star',
            'Music', 'Mountain', 'Clock', 'Coffee', 'Table', 'Chair', 'Phone', 'Picture', 'Hat', 'Apple',
            'Glass', 'Plate', 'Television', 'Bag', 'Shoe', 'Pants', 'Jacket', 'Glasses', 'Lamp',
            'Map', 'Building', 'Bridge', 'Train', 'Car', 'Bicycle', 'Plane', 'Balloon', 'House', 'Street', 'Park',
            'Garden', 'Child', 'Baby', 'Rain', 'Snow', 'Sun', 'Sand', 'Cloud', 'Bird', 'Fish', 'Lake', 'River',
            'Forest', 'Island', 'Lighthouse', 'Route', 'Bus', 'Calendar', 'Notebook', 'Pencil case', 'Eraser', 'Paint', 'Brush',
            'Canvas', 'Kitchen', 'Bathroom', 'Bed', 'Room', 'Living room', 'Corridor', 'Frame', 'Lock', 'Key', 'Fruit',
            'Vegetable', 'Chocolate', 'Ice cream', 'Cake', 'Bread', 'Cheese', 'Olive', 'Tomato', 'Cucumber', 'Pepper',
            'Potato', 'Carrot', 'Onion', 'Garlic', 'Parsley', 'Dill', 'Mint', 'Lemon', 'Orange', 'Tangerine',
            'Watermelon', 'Melon', 'Cherry', 'Strawberry', 'Banana', 'Grape', 'Apple', 'Pear'
        ]

        self.word = choice(self.words).lower()
        self.prediction = ['_'] * len(self.word)
        self.accuracy = False

        self.layout = QVBoxLayout()

        self.word_label = QLabel(' '.join(self.prediction), self)
        self.word_label.setFont(QFont('Arial', 24))
        self.layout.addWidget(self.word_label)

        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText('Harf veya tahmininizi giriniz...')
        self.layout.addWidget(self.input_line)

        self.guess_button = QPushButton('Tahmin Et', self)
        self.guess_button.clicked.connect(self.guess)
        self.layout.addWidget(self.guess_button)

        self.new_game_button = QPushButton('Yeni Oyun', self)
        self.new_game_button.clicked.connect(self.new_game)
        self.layout.addWidget(self.new_game_button)

        self.setLayout(self.layout)

    def guess(self):
        inp1 = self.input_line.text().lower()
        self.input_line.clear()

        if inp1 == 'tahmin':
            inp2, ok = QInputDialog.getText(self, 'Tahmin', 'Tahmininizi giriniz:')
            if ok:
                inp2 = inp2.lower()
                if inp2 == self.word:
                    QMessageBox.information(self, 'Tebrikler', f"Tebrikler, kelimemiz: {self.word}")
                    self.accuracy = True
                else:
                    QMessageBox.warning(self, 'Yanlış', 'Yanlış tahmin, tekrar deneyin')
            return

        if inp1 in self.word:
            for i, letter in enumerate(self.word):
                if letter == inp1:
                    self.prediction[i] = letter

            self.word_label.setText(' '.join(self.prediction))

            if '_' not in self.prediction:
                QMessageBox.information(self, 'Tebrikler', f"Tebrikler, kelimeyi buldunuz: {self.word}")
                self.accuracy = True

        else:
            QMessageBox.warning(self, 'Yanlış', 'Yanlış harf, tekrar deneyin')

    def new_game(self):
        self.word = choice(self.words).lower()
        self.prediction = ['_'] * len(self.word)
        self.accuracy = False
        self.word_label.setText(' '.join(self.prediction))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = WordGuessingGame()
    game.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont
from random import choice

class WordGuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kelime Tahmin Oyunu')
        self.setGeometry(100, 100, 500, 300)

        self.words = [
            'GalataSaray', 'Book', 'Wind', 'Pen', 'Flower', 'Computer', 'Sea', 'Cat', 'Tree', 'Star',
            'Music', 'Mountain', 'Clock', 'Coffee', 'Table', 'Chair', 'Phone', 'Picture', 'Hat', 'Apple',
            'Glass', 'Plate', 'Television', 'Bag', 'Shoe', 'Pants', 'Jacket', 'Glasses', 'Lamp',
            'Map', 'Building', 'Bridge', 'Train', 'Car', 'Bicycle', 'Plane', 'Balloon', 'House', 'Street', 'Park',
            'Garden', 'Child', 'Baby', 'Rain', 'Snow', 'Sun', 'Sand', 'Cloud', 'Bird', 'Fish', 'Lake', 'River',
            'Forest', 'Island', 'Lighthouse', 'Route', 'Bus', 'Calendar', 'Notebook', 'Pencil case', 'Eraser', 'Paint', 'Brush',
            'Canvas', 'Kitchen', 'Bathroom', 'Bed', 'Room', 'Living room', 'Corridor', 'Frame', 'Lock', 'Key', 'Fruit',
            'Vegetable', 'Chocolate', 'Ice cream', 'Cake', 'Bread', 'Cheese', 'Olive', 'Tomato', 'Cucumber', 'Pepper',
            'Potato', 'Carrot', 'Onion', 'Garlic', 'Parsley', 'Dill', 'Mint', 'Lemon', 'Orange', 'Tangerine',
            'Watermelon', 'Melon', 'Cherry', 'Strawberry', 'Banana', 'Grape', 'Apple', 'Pear'
        ]

        self.word = choice(self.words).lower()
        self.prediction = ['_'] * len(self.word)
        self.accuracy = False

        self.layout = QVBoxLayout()

        self.word_label = QLabel(' '.join(self.prediction), self)
        self.word_label.setFont(QFont('Arial', 24))
        self.layout.addWidget(self.word_label)

        # Harf tahmini için giriş alanı ve buton
        self.letter_input = QLineEdit(self)
        self.letter_input.setPlaceholderText('Harf giriniz...')
        self.layout.addWidget(self.letter_input)

        self.letter_button = QPushButton('Harf Tahmini', self)
        self.letter_button.clicked.connect(self.guess_letter)
        self.layout.addWidget(self.letter_button)

        # Kelime tahmini için giriş alanı ve buton
        self.word_input = QLineEdit(self)
        self.word_input.setPlaceholderText('Kelimeyi tahmin ediniz...')
        self.layout.addWidget(self.word_input)

        self.word_button = QPushButton('Kelime Tahmini', self)
        self.word_button.clicked.connect(self.guess_word)
        self.layout.addWidget(self.word_button)

        # Yeni oyun ve çıkış butonları
        self.button_layout = QHBoxLayout()

        self.new_game_button = QPushButton('Yeni Oyun', self)
        self.new_game_button.clicked.connect(self.new_game)
        self.button_layout.addWidget(self.new_game_button)

        self.exit_button = QPushButton('Çıkış', self)
        self.exit_button.clicked.connect(self.close)
        self.button_layout.addWidget(self.exit_button)

        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

    def guess_letter(self):
        letter = self.letter_input.text().lower()
        self.letter_input.clear()

        if len(letter) != 1 or not letter.isalpha():
            QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
            return

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.prediction[i] = letter

            self.word_label.setText(' '.join(self.prediction))

            if '_' not in self.prediction:
                self.game_over()

        else:
            QMessageBox.warning(self, 'Yanlış', 'Bu harf kelime içinde yok.')

    def guess_word(self):
        word = self.word_input.text().lower()
        self.word_input.clear()

        if word == self.word:
            self.prediction = list(self.word)
            self.word_label.setText(' '.join(self.prediction))
            self.game_over()

        else:
            QMessageBox.warning(self, 'Yanlış', 'Yanlış tahmin, tekrar deneyin.')

    def game_over(self):
        QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.word}')
        self.accuracy = True

    def new_game(self):
        self.word = choice(self.words).lower()
        self.prediction = ['_'] * len(self.word)
        self.accuracy = False
        self.word_label.setText(' '.join(self.prediction))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Çıkış', 'Oyundan çıkmak istediğinizden emin misiniz?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = WordGuessingGame()
    game.show()
    sys.exit(app.exec_())

'''

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from random import choice

# class WordGuessingGame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Kelime Tahmin Oyunu')
#         self.setGeometry(100, 100, 500, 300)

#         self.kelimeler = [
#             'Galatasaray', 'Kitap', 'Rüzgar', 'Kalem', 'Çiçek', 'Bilgisayar', 'Deniz', 'Kedi', 'Ağaç', 'Yıldız',
#             'Müzik', 'Dağ', 'Saat', 'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Resim', 'Şapka', 'Elma',
#             'Cam', 'Tabak', 'Televizyon', 'Çanta', 'Ayakkabı', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba',
#             'Harita', 'Bina', 'Köprü', 'Tren', 'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Ev', 'Cadde', 'Park',
#             'Bahçe', 'Çocuk', 'Bebek', 'Yağmur', 'Kar', 'Güneş', 'Kum', 'Bulut', 'Kuş', 'Balık', 'Göl', 'Nehir',
#             'Orman', 'Ada', 'Deniz Feneri', 'Rota', 'Otobüs', 'Takvim', 'Defter', 'Kalem Kutusu', 'Silgi', 'Boya', 'Fırça',
#             'Tuval', 'Mutfak', 'Banyo', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve', 'Kilit', 'Anahtar', 'Meyve',
#             'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber',
#             'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu', 'Nane', 'Limon', 'Portakal', 'Mandalina',
#             'Karpuz', 'Kavun', 'Kiraz', 'Çilek', 'Muz', 'Üzüm', 'Elma', 'Armut'
#         ]

#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.doğruluk = False

#         self.düzen = QVBoxLayout()

#         self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
#         self.kelime_etiket.setFont(QFont('Arial', 24))
#         self.düzen.addWidget(self.kelime_etiket)

#         # Harf tahmini için giriş alanı ve buton
#         self.harf_girişi = QLineEdit(self)
#         self.harf_girişi.setPlaceholderText('Harf giriniz...')
#         self.düzen.addWidget(self.harf_girişi)

#         self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
#         self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
#         self.düzen.addWidget(self.harf_tahmin_butonu)

#         # Kelime tahmini için giriş alanı ve buton
#         self.kelime_girişi = QLineEdit(self)
#         self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
#         self.düzen.addWidget(self.kelime_girişi)

#         self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
#         self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
#         self.düzen.addWidget(self.kelime_tahmin_butonu)

#         # Yeni oyun ve çıkış butonları
#         self.buton_düzeni = QHBoxLayout()

#         self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
#         self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
#         self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

#         self.çıkış_butonu = QPushButton('Çıkış', self)
#         self.çıkış_butonu.clicked.connect(self.close)
#         self.buton_düzeni.addWidget(self.çıkış_butonu)

#         self.düzen.addLayout(self.buton_düzeni)

#         self.setLayout(self.düzen)

#     def harf_tahmini(self):
#         harf = self.harf_girişi.text().upper()
#         self.harf_girişi.clear()

#         if len(harf) != 1 or not harf.isalpha():
#             QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
#             return

#         if harf in self.kelime:
#             for i, karakter in enumerate(self.kelime):
#                 if karakter == harf:
#                     self.tahmin[i] = harf

#             self.kelime_etiket.setText(' '.join(self.tahmin))

#             if '_' not in self.tahmin:
#                 self.oyun_sonu()

#         else:
#             self.harf_girişi.setPlaceholderText('Yanlış harf tahmini.')

#     def kelime_tahmini(self):
#         kelime = self.kelime_girişi.text().upper()
#         self.kelime_girişi.clear()

#         if kelime == self.kelime:
#             self.tahmin = list(self.kelime)
#             self.kelime_etiket.setText(' '.join(self.tahmin))
#             self.oyun_sonu()

#         else:
#             QMessageBox.warning(self, 'Yanlış', 'Yanlış tahmin, tekrar deneyin.')

#     def oyun_sonu(self):
#         QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')
#         self.doğruluk = True

#     def yeni_oyun(self):
#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.doğruluk = False
#         self.kelime_etiket.setText(' '.join(self.tahmin))

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = WordGuessingGame()
#     oyun.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from random import choice

# class WordGuessingGame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Kelime Tahmin Oyunu')
#         self.setGeometry(100, 100, 500, 300)

#         self.kelimeler = [
#             'Galatasaray', 'Kitap', 'Rüzgar', 'Kalem', 'Çiçek', 'Bilgisayar', 'Deniz', 'Kedi', 'Ağaç', 'Yıldız',
#             'Müzik', 'Dağ', 'Saat', 'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Resim', 'Şapka', 'Elma',
#             'Cam', 'Tabak', 'Televizyon', 'Çanta', 'Ayakkabı', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba',
#             'Harita', 'Bina', 'Köprü', 'Tren', 'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Ev', 'Cadde', 'Park',
#             'Bahçe', 'Çocuk', 'Bebek', 'Yağmur', 'Kar', 'Güneş', 'Kum', 'Bulut', 'Kuş', 'Balık', 'Göl', 'Nehir',
#             'Orman', 'Ada', 'Deniz Feneri', 'Rota', 'Otobüs', 'Takvim', 'Defter', 'Kalem Kutusu', 'Silgi', 'Boya', 'Fırça',
#             'Tuval', 'Mutfak', 'Banyo', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve', 'Kilit', 'Anahtar', 'Meyve',
#             'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber',
#             'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu', 'Nane', 'Limon', 'Portakal', 'Mandalina',
#             'Karpuz', 'Kavun', 'Kiraz', 'Çilek', 'Muz', 'Üzüm', 'Elma', 'Armut'
#         ]

#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 5

#         self.düzen = QVBoxLayout()

#         self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
#         self.kelime_etiket.setFont(QFont('Arial', 24))
#         self.düzen.addWidget(self.kelime_etiket)

#         self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
#         self.hak_etiket.setFont(QFont('Arial', 14))
#         self.düzen.addWidget(self.hak_etiket)

#         # Harf tahmini için giriş alanı ve buton
#         self.harf_girişi = QLineEdit(self)
#         self.harf_girişi.setPlaceholderText('Harf giriniz...')
#         self.düzen.addWidget(self.harf_girişi)

#         self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
#         self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
#         self.düzen.addWidget(self.harf_tahmin_butonu)

#         # Kelime tahmini için giriş alanı ve buton
#         self.kelime_girişi = QLineEdit(self)
#         self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
#         self.düzen.addWidget(self.kelime_girişi)

#         self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
#         self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
#         self.düzen.addWidget(self.kelime_tahmin_butonu)

#         # Yeni oyun ve çıkış butonları
#         self.buton_düzeni = QHBoxLayout()

#         self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
#         self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
#         self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

#         self.çıkış_butonu = QPushButton('Çıkış', self)
#         self.çıkış_butonu.clicked.connect(self.close)
#         self.buton_düzeni.addWidget(self.çıkış_butonu)

#         self.düzen.addLayout(self.buton_düzeni)

#         self.setLayout(self.düzen)

#     def harf_tahmini(self):
#         harf = self.harf_girişi.text().upper()
#         self.harf_girişi.clear()

#         if len(harf) != 1 or not harf.isalpha():
#             QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
#             return

#         if harf in self.kelime:
#             for i, karakter in enumerate(self.kelime):
#                 if karakter == harf:
#                     self.tahmin[i] = harf

#             self.kelime_etiket.setText(' '.join(self.tahmin))

#             if '_' not in self.tahmin:
#                 self.oyun_sonu()
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.harf_girişi.setPlaceholderText('Yanlış harf tahmini.')
#             if self.hak == 0:
#                 self.hak_bitti()

#     def kelime_tahmini(self):
#         kelime = self.kelime_girişi.text().upper()
#         self.kelime_girişi.clear()

#         if kelime == self.kelime:
#             self.tahmin = list(self.kelime)
#             self.kelime_etiket.setText(' '.join(self.tahmin))
#             self.oyun_sonu()
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             QMessageBox.warning(self, 'Yanlış', 'Yanlış tahmin, tekrar deneyin.')
#             if self.hak == 0:
#                 self.hak_bitti()

#     def oyun_sonu(self):
#         QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')

#     def hak_bitti(self):
#         QMessageBox.critical(self, 'Oyun Bitti', f'Haklarınız bitti. Kelime: {self.kelime}')
#         self.yeni_oyun()

#     def yeni_oyun(self):
#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 5
#         self.kelime_etiket.setText(' '.join(self.tahmin))
#         self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = WordGuessingGame()
#     oyun.show()
#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from random import choice

# class WordGuessingGame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Adam Asmaca')
#         self.setGeometry(100, 100, 500, 400)

#         self.kelimeler = [
#             'Galatasaray', 'Kitap', 'Rüzgar', 'Kalem', 'Çiçek', 'Bilgisayar', 'Deniz', 'Kedi', 'Ağaç', 'Yıldız',
#             'Müzik', 'Dağ', 'Saat', 'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Resim', 'Şapka', 'Elma',
#             'Cam', 'Tabak', 'Televizyon', 'Çanta', 'Ayakkabı', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba',
#             'Harita', 'Bina', 'Köprü', 'Tren', 'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Ev', 'Cadde', 'Park',
#             'Bahçe', 'Çocuk', 'Bebek', 'Yağmur', 'Kar', 'Güneş', 'Kum', 'Bulut', 'Kuş', 'Balık', 'Göl', 'Nehir',
#             'Orman', 'Ada', 'Deniz Feneri', 'Rota', 'Otobüs', 'Takvim', 'Defter', 'Kalem Kutusu', 'Silgi', 'Boya', 'Fırça',
#             'Tuval', 'Mutfak', 'Banyo', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve', 'Kilit', 'Anahtar', 'Meyve',
#             'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber',
#             'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu', 'Nane', 'Limon', 'Portakal', 'Mandalina',
#             'Karpuz', 'Kavun', 'Kiraz', 'Çilek', 'Muz', 'Üzüm', 'Elma', 'Armut'
#         ]

#         self.ascii_stages = [
#             """
#                 +---+
#                     |
#                     |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                     |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                 |   |
#                 |   |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|   |
#                 |   |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|\  |
#                 |   |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|\  |
#                 |   |
#                /   ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|\  |
#                 |   |
#                / \ ===
#             """
#         ]

#         self.face_expressions = [
#             'O',
#             'O',
#             'O',
#             'O',
#             'O',
#             'O',
#             'X'
#         ]

#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6

#         self.düzen = QVBoxLayout()

#         self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
#         self.kelime_etiket.setFont(QFont('Arial', 24))
#         self.düzen.addWidget(self.kelime_etiket)

#         self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
#         self.hak_etiket.setFont(QFont('Arial', 14))
#         self.düzen.addWidget(self.hak_etiket)

#         self.ascii_etiket = QLabel(self.ascii_stages[0], self)
#         self.ascii_etiket.setFont(QFont('Courier', 18))
#         self.düzen.addWidget(self.ascii_etiket)

#         # Harf tahmini için giriş alanı ve buton
#         self.harf_girişi = QLineEdit(self)
#         self.harf_girişi.setPlaceholderText('Harf giriniz...')
#         self.düzen.addWidget(self.harf_girişi)

#         self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
#         self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
#         self.düzen.addWidget(self.harf_tahmin_butonu)

#         # Kelime tahmini için giriş alanı ve buton
#         self.kelime_girişi = QLineEdit(self)
#         self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
#         self.düzen.addWidget(self.kelime_girişi)

#         self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
#         self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
#         self.düzen.addWidget(self.kelime_tahmin_butonu)

#         # Yeni oyun ve çıkış butonları
#         self.buton_düzeni = QHBoxLayout()

#         self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
#         self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
#         self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

#         self.çıkış_butonu = QPushButton('Çıkış', self)
#         self.çıkış_butonu.clicked.connect(self.close)
#         self.buton_düzeni.addWidget(self.çıkış_butonu)

#         self.düzen.addLayout(self.buton_düzeni)

#         self.setLayout(self.düzen)

#     def harf_tahmini(self):
#         harf = self.harf_girişi.text().upper()
#         self.harf_girişi.clear()

#         if len(harf) != 1 or not harf.isalpha():
#             QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
#             return

#         if harf in self.kelime:
#             for i, karakter in enumerate(self.kelime):
#                 if karakter == harf:
#                     self.tahmin[i] = harf

#             self.kelime_etiket.setText(' '.join(self.tahmin))

#             if '_' not in self.tahmin:
#                 self.oyun_sonu()
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak].replace('O', self.face_expressions[6 - self.hak]))
#             self.harf_girişi.setPlaceholderText('Yanlış harf tahmini.')
#             if self.hak == 0:
#                 self.hak_bitti()

#     def kelime_tahmini(self):
#         kelime = self.kelime_girişi.text().upper()
#         self.kelime_girişi.clear()

#         if kelime == self.kelime:
#             self.tahmin = list(self.kelime)
#             self.kelime_etiket.setText(' '.join(self.tahmin))
#             self.oyun_sonu()
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak].replace('O', self.face_expressions[6 - self.hak]))
#             QMessageBox.warning(self, 'Yanlış', 'Yanlış tahmin, tekrar deneyin.')
#             if self.hak == 0:
#                 self.hak_bitti()

#     def oyun_sonu(self):
#         QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')

#     def hak_bitti(self):
#         QMessageBox.critical(self, 'Oyun Bitti', f'Haklarınız bitti. Kelime: {self.kelime}')
#         self.yeni_oyun()

#     def yeni_oyun(self):
#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6
#         self.kelime_etiket.setText(' '.join(self.tahmin))
#         self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#         self.ascii_etiket.setText(self.ascii_stages[0])

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = WordGuessingGame()
#     oyun.show()
#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from random import choice

# class WordGuessingGame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Adam Asmaca')
#         self.setGeometry(100, 100, 700, 400)

#         self.kelimeler = [
#             'Galatasaray', 'Kitap', 'Rüzgar', 'Kalem', 'Çiçek', 'Bilgisayar', 'Deniz', 'Kedi', 'Ağaç', 'Yıldız',
#             'Müzik', 'Dağ', 'Saat', 'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Resim', 'Şapka', 'Elma',
#             'Cam', 'Tabak', 'Televizyon', 'Çanta', 'Ayakkabı', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba',
#             'Harita', 'Bina', 'Köprü', 'Tren', 'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Ev', 'Cadde', 'Park',
#             'Bahçe', 'Çocuk', 'Bebek', 'Yağmur', 'Kar', 'Güneş', 'Kum', 'Bulut', 'Kuş', 'Balık', 'Göl', 'Nehir',
#             'Orman', 'Ada', 'Deniz Feneri', 'Rota', 'Otobüs', 'Takvim', 'Defter', 'Kalem Kutusu', 'Silgi', 'Boya', 'Fırça',
#             'Tuval', 'Mutfak', 'Banyo', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve', 'Kilit', 'Anahtar', 'Meyve',
#             'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber',
#             'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu', 'Nane', 'Limon', 'Portakal', 'Mandalina',
#             'Karpuz', 'Kavun', 'Kiraz', 'Çilek', 'Muz', 'Üzüm', 'Elma', 'Armut'
#         ]

#         self.ascii_stages = [
#             """
#                 +---+
#                     |
#                     |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                     |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                 |   |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|   |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|\  |
#                     |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|\  |
#                /    |
#                    ===
#             """,
#             """
#                 +---+
#                 O   |
#                /|\  |
#                / \  |
#                    ===
#             """
#         ]

#         self.face_expressions = [
#             'O',
#             'O',
#             'O',
#             'O',
#             'O',
#             'O',
#             'X'
#         ]

#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6

#         self.düzen = QHBoxLayout()

#         self.sol_düzen = QVBoxLayout()

#         self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
#         self.kelime_etiket.setFont(QFont('Arial', 24))
#         self.sol_düzen.addWidget(self.kelime_etiket)

#         self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
#         self.hak_etiket.setFont(QFont('Arial', 14))
#         self.sol_düzen.addWidget(self.hak_etiket)

#         # Harf tahmini için giriş alanı ve buton
#         self.harf_girişi = QLineEdit(self)
#         self.harf_girişi.setPlaceholderText('Harf giriniz...')
#         self.sol_düzen.addWidget(self.harf_girişi)

#         self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
#         self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
#         self.sol_düzen.addWidget(self.harf_tahmin_butonu)

#         # Kelime tahmini için giriş alanı ve buton
#         self.kelime_girişi = QLineEdit(self)
#         self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
#         self.sol_düzen.addWidget(self.kelime_girişi)

#         self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
#         self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
#         self.sol_düzen.addWidget(self.kelime_tahmin_butonu)

#         # Yeni oyun ve çıkış butonları
#         self.buton_düzeni = QHBoxLayout()

#         self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
#         self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
#         self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

#         self.çıkış_butonu = QPushButton('Çıkış', self)
#         self.çıkış_butonu.clicked.connect(self.close)
#         self.buton_düzeni.addWidget(self.çıkış_butonu)

#         self.sol_düzen.addLayout(self.buton_düzeni)

#         self.düzen.addLayout(self.sol_düzen)

#         self.ascii_etiket = QLabel(self.ascii_stages[0], self)
#         self.ascii_etiket.setFont(QFont('Courier', 18))
#         self.düzen.addWidget(self.ascii_etiket)

#         self.setLayout(self.düzen)

#     def harf_tahmini(self):
#         harf = self.harf_girişi.text().upper()
#         self.harf_girişi.clear()

#         if len(harf) != 1 or not harf.isalpha():
#             QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
#             return

#         if harf in self.kelime:
#             for i, karakter in enumerate(self.kelime):
#                 if karakter == harf:
#                     self.tahmin[i] = harf

#             self.kelime_etiket.setText(' '.join(self.tahmin))

#             if '_' not in self.tahmin:
#                 self.oyun_sonu()
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak].replace('O', self.face_expressions[6 - self.hak]))
#             self.harf_girişi.setPlaceholderText('Yanlış harf tahmini.')
#             if self.hak == 0:
#                 self.hak_bitti()

#     def kelime_tahmini(self):
#         kelime = self.kelime_girişi.text().upper()
#         self.kelime_girişi.clear()

#         if kelime == self.kelime:
#             self.tahmin = list(self.kelime)
#             self.kelime_etiket.setText(' '.join(self.tahmin))
#             self.oyun_sonu()
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak].replace('O', self.face_expressions[6 - self.hak]))
#             QMessageBox.warning(self, 'Yanlış', 'Yanlış tahmin, tekrar deneyin.')
#             if self.hak == 0:
#                 self.hak_bitti()

#     def oyun_sonu(self):
#         QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')

#     def hak_bitti(self):
#         QMessageBox.critical(self, 'Oyun Bitti', f'Haklarınız bitti. Kelime: {self.kelime}')
#         self.yeni_oyun()

#     def yeni_oyun(self):
#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6
#         self.kelime_etiket.setText(' '.join(self.tahmin))
#         self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#         self.ascii_etiket.setText(self.ascii_stages[0])

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = WordGuessingGame()
#     oyun.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from random import choice

# class WordGuessingGame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Adam Asmaca')
#         self.setGeometry(100, 100, 800, 400)

#         self.kelimeler = [
#             'Galatasaray', 'Kitap', 'Rüzgar', 'Kalem', 'Çiçek', 'Bilgisayar', 'Deniz', 'Kedi', 'Ağaç', 'Yıldız',
#             'Müzik', 'Dağ', 'Saat', 'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Resim', 'Şapka', 'Elma',
#             'Cam', 'Tabak', 'Televizyon', 'Çanta', 'Ayakkabı', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba',
#             'Harita', 'Bina', 'Köprü', 'Tren', 'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Ev', 'Cadde', 'Park',
#             'Bahçe', 'Çocuk', 'Bebek', 'Yağmur', 'Kar', 'Güneş', 'Kum', 'Bulut', 'Kuş', 'Balık', 'Göl', 'Nehir',
#             'Orman', 'Ada', 'Deniz Feneri', 'Rota', 'Otobüs', 'Takvim', 'Defter', 'Kalem Kutusu', 'Silgi', 'Boya', 'Fırça',
#             'Tuval', 'Mutfak', 'Banyo', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve', 'Kilit', 'Anahtar', 'Meyve',
#             'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber',
#             'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu', 'Nane', 'Limon', 'Portakal', 'Mandalina',
#             'Karpuz', 'Kavun', 'Kiraz', 'Çilek', 'Muz', 'Üzüm', 'Elma', 'Armut'
#         ]

#         self.ascii_stages = [
#             "  \n\n\n\n\n\n\n",
#             "  +---+\n      |\n      |\n      |\n      |\n      |\n========= \n",
#             "  +---+\n  O   |\n      |\n      |\n      |\n      |\n========= \n",
#             "  +---+\n  O   |\n  |   |\n      |\n      |\n      |\n========= \n",
#             "  +---+\n  O   |\n /|   |\n      |\n      |\n      |\n========= \n",
#             "  +---+\n  O   |\n /|\\  |\n      |\n      |\n      |\n========= \n",
#             "  +---+\n  O   |\n /|\\  |\n /    |\n      |\n      |\n========= \n",
#             "  +---+\n  O   |\n /|\\  |\n / \\  |\n      |\n      |\n========= \n"
#         ]

#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6

#         self.düzen = QHBoxLayout()
#         self.sol_düzen = QVBoxLayout()

#         self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
#         self.kelime_etiket.setFont(QFont('Arial', 24))
#         self.sol_düzen.addWidget(self.kelime_etiket)

#         self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
#         self.hak_etiket.setFont(QFont('Arial', 14))
#         self.sol_düzen.addWidget(self.hak_etiket)

#         self.harf_girişi = QLineEdit(self)
#         self.harf_girişi.setPlaceholderText('Harf giriniz...')
#         self.sol_düzen.addWidget(self.harf_girişi)

#         self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
#         self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
#         self.sol_düzen.addWidget(self.harf_tahmin_butonu)

#         self.kelime_girişi = QLineEdit(self)
#         self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
#         self.sol_düzen.addWidget(self.kelime_girişi)

#         self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
#         self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
#         self.sol_düzen.addWidget(self.kelime_tahmin_butonu)

#         self.buton_düzeni = QHBoxLayout()

#         self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
#         self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
#         self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

#         self.çıkış_butonu = QPushButton('Çıkış', self)
#         self.çıkış_butonu.clicked.connect(self.close)
#         self.buton_düzeni.addWidget(self.çıkış_butonu)

#         self.sol_düzen.addLayout(self.buton_düzeni)

#         self.ascii_etiket = QLabel(self)
#         self.ascii_etiket.setFont(QFont('Courier', 18))
#         self.ascii_etiket.setText(self.ascii_stages[0])

#         self.düzen.addLayout(self.sol_düzen)
#         self.düzen.addWidget(self.ascii_etiket)
        
#         self.setLayout(self.düzen)

#     def harf_tahmini(self):
#         harf = self.harf_girişi.text().upper()
#         self.harf_girişi.clear()

#         if len(harf) != 1 or not harf.isalpha():
#             QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
#             return

#         if harf in self.tahmin:
#             QMessageBox.warning(self, 'Hata', 'Bu harfi zaten tahmin ettiniz.')
#             return

#         if harf in self.kelime:
#             for i, karakter in enumerate(self.kelime):
#                 if karakter == harf:
#                     self.tahmin[i] = harf

#             self.kelime_etiket.setText(' '.join(self.tahmin))

#             if '_' not in self.tahmin:
#                 self.oyun_sonu(True)
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

#             if self.hak == 0:
#                 self.oyun_sonu(False)

#     def kelime_tahmini(self):
#         kelime = self.kelime_girişi.text().upper()
#         self.kelime_girişi.clear()

#         if kelime == self.kelime:
#             self.tahmin = list(self.kelime)
#             self.kelime_etiket.setText(' '.join(self.tahmin))
#             self.oyun_sonu(True)
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

#             if self.hak == 0:
#                 self.oyun_sonu(False)

#     def oyun_sonu(self, kazandi):
#         if kazandi:
#             QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')
#         else:
#             QMessageBox.warning(self, 'Kaybettiniz', f'Hakkınız bitti, kelime: {self.kelime}')
#         self.yeni_oyun()

#     def yeni_oyun(self):
#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6
#         self.kelime_etiket.setText(' '.join(self.tahmin))
#         self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#         self.ascii_etiket.setText(self.ascii_stages[0])

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = WordGuessingGame()
#     oyun.show()
#     sys.exit(app.exec_())




# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from random import choice

# class WordGuessingGame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Adam Asmaca')
#         self.setGeometry(100, 100, 800, 400)

#         self.kelimeler = [
#             'Galatasaray', 'Kitap', 'Rüzgar', 'Kalem', 'Çiçek', 'Bilgisayar', 'Deniz', 'Kedi', 'Ağaç', 'Yıldız',
#             'Müzik', 'Dağ', 'Saat', 'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Resim', 'Şapka', 'Elma',
#             'Cam', 'Tabak', 'Televizyon', 'Çanta', 'Ayakkabı', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba',
#             'Harita', 'Bina', 'Köprü', 'Tren', 'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Ev', 'Cadde', 'Park',
#             'Bahçe', 'Çocuk', 'Bebek', 'Yağmur', 'Kar', 'Güneş', 'Kum', 'Bulut', 'Kuş', 'Balık', 'Göl', 'Nehir',
#             'Orman', 'Ada', 'Deniz Feneri', 'Rota', 'Otobüs', 'Takvim', 'Defter', 'Kalem Kutusu', 'Silgi', 'Boya', 'Fırça',
#             'Tuval', 'Mutfak', 'Banyo', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve', 'Kilit', 'Anahtar', 'Meyve',
#             'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber',
#             'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu', 'Nane', 'Limon', 'Portakal', 'Mandalina',
#             'Karpuz', 'Kavun', 'Kiraz', 'Çilek', 'Muz', 'Üzüm', 'Elma', 'Armut'
#         ]

        # self.ascii_stages = [
        #     """
        #         +---+
        #             |
        #             |
        #             |
        #            ===
        #     """,
        #     """
        #         +---+
        #         O   |
        #             |
        #             |
        #            ===
        #     """,
        #     """
        #         +---+
        #         O   |
        #         |   |
        #         |   |
        #            ===
        #     """,
        #     """
        #         +---+
        #         O   |
        #        /|   |
        #         |   |
        #            ===
        #     """,
        #     """
        #         +---+
        #         O   |
        #        /|\  |
        #         |   |
        #            ===
        #     """,
        #     """
        #         +---+
        #         O   |
        #        /|\  |
        #         |   |
        #        /   ===
        #     """,
        #     """
        #         +---+
        #         O   |
        #        /|\  |
        #         |   |
        #        / \ ===
        #     """
        # ]

#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6

#         self.düzen = QHBoxLayout()
#         self.sol_düzen = QVBoxLayout()

#         self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
#         self.kelime_etiket.setFont(QFont('Arial', 24))
#         self.sol_düzen.addWidget(self.kelime_etiket)

#         self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
#         self.hak_etiket.setFont(QFont('Arial', 14))
#         self.sol_düzen.addWidget(self.hak_etiket)

#         # Harf tahmini için giriş alanı ve buton
#         self.harf_girişi = QLineEdit(self)
#         self.harf_girişi.setPlaceholderText('Harf giriniz...')
#         self.sol_düzen.addWidget(self.harf_girişi)

#         self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
#         self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
#         self.sol_düzen.addWidget(self.harf_tahmin_butonu)

#         # Kelime tahmini için giriş alanı ve buton
#         self.kelime_girişi = QLineEdit(self)
#         self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
#         self.sol_düzen.addWidget(self.kelime_girişi)

#         self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
#         self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
#         self.sol_düzen.addWidget(self.kelime_tahmin_butonu)

#         # Yeni oyun ve çıkış butonları
#         self.buton_düzeni = QHBoxLayout()

#         self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
#         self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
#         self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

#         self.çıkış_butonu = QPushButton('Çıkış', self)
#         self.çıkış_butonu.clicked.connect(self.close)
#         self.buton_düzeni.addWidget(self.çıkış_butonu)

#         self.sol_düzen.addLayout(self.buton_düzeni)

#         self.ascii_etiket = QLabel(self)
#         self.ascii_etiket.setFont(QFont('Courier', 18))
#         self.ascii_etiket.setText(self.ascii_stages[0])

#         self.düzen.addLayout(self.sol_düzen)
#         self.düzen.addWidget(self.ascii_etiket)
        
#         self.setLayout(self.düzen)

#     def harf_tahmini(self):
#         harf = self.harf_girişi.text().upper()
#         self.harf_girişi.clear()

#         if len(harf) != 1 or not harf.isalpha():
#             QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
#             return

#         if harf in self.kelime:
#             for i, karakter in enumerate(self.kelime):
#                 if karakter == harf:
#                     self.tahmin[i] = harf

#             self.kelime_etiket.setText(' '.join(self.tahmin))

#             if '_' not in self.tahmin:
#                 self.oyun_sonu(True)
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

#             if self.hak == 0:
#                 self.oyun_sonu(False)

#     def kelime_tahmini(self):
#         kelime = self.kelime_girişi.text().upper()
#         self.kelime_girişi.clear()

#         if kelime == self.kelime:
#             self.tahmin = list(self.kelime)
#             self.kelime_etiket.setText(' '.join(self.tahmin))
#             self.oyun_sonu(True)
#         else:
#             self.hak -= 1
#             self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#             self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

#             if self.hak == 0:
#                 self.oyun_sonu(False)

#     def oyun_sonu(self, kazandi):
#         if kazandi:
#             QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')
#         else:
#             QMessageBox.warning(self, 'Kaybettiniz', f'Hakkınız bitti, kelime: {self.kelime}')
#         self.yeni_oyun()

#     def yeni_oyun(self):
#         self.kelime = choice(self.kelimeler).upper()
#         self.tahmin = ['_'] * len(self.kelime)
#         self.hak = 6
#         self.kelime_etiket.setText(' '.join(self.tahmin))
#         self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
#         self.ascii_etiket.setText(self.ascii_stages[0])

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = WordGuessingGame()
#     oyun.show()
#     sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from PyQt5.QtGui import QFont
from random import choice

class WordGuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Adam Asmaca')
        self.setGeometry(100, 100, 800, 400)

        # Oyun kelimeleri ve zorluk seviyeleri
        self.kelimeler = {
    'Kolay': [
        'Elma', 'Kedi', 'Göl', 'Çiçek', 'Kalem', 'Deniz', 'Ağaç', 'Yıldız', 'Müzik', 'Saat',
        'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Şapka', 'Cam', 'Tabak', 'Çanta', 'Ayakkabı', 'Bebek',
        'Kuş', 'Balık', 'Göl', 'Nehir', 'Çocuk', 'Kar', 'Güneş', 'Kavun', 'Kiraz', 'Çilek',
        'Muz', 'Üzüm', 'Armut', 'Ev', 'Park', 'Bahçe', 'Elma', 'Kum', 'Bulut', 'Boya',
        'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber', 'Patates', 'Havuç', 'Soğan', 'Nane'
    ],
    'Orta': [
        'Bilgisayar', 'Çanta', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba', 'Harita', 'Bina', 'Köprü', 'Tren',
        'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Cadde', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve',
        'Anahtar', 'Meyve', 'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Mandalina',
        'Karpuz', 'Kavun', 'Salatalık', 'Biber', 'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu'
    ],
    'Zor': [
        'Galatasaray', 'Bilgisayar', 'Televizyon', 'Kütüphane', 'Fenerbahçe', 'Müze', 'Eczane', 'Şehir',
        'Otobüs', 'Kütüphane', 'Tiyatro', 'Yıldız', 'Müzikal', 'Deniz Feneri', 'Rota', 'Kalem Kutusu', 'Silgi', 'Fırça',
        'Tuval', 'Mutfak', 'Banyo', 'Kalem Kutusu', 'Silgi', 'Fırça', 'Rota', 'Harita', 'Kütüphane', 'Yüksek Hızlı Tren'
    ]
}
        
        self.ascii_stages = [
            """
                +---+
                    |
                    |
                    |
                   ===
            """,
            """
                +---+
                O   |
                    |
                    |
                   ===
            """,
            """
                +---+
                O   |
                |   |
                |   |
                   ===
            """,
            """
                +---+
                O   |
               /|   |
                |   |
                   ===
            """,
            """
                +---+
                O   |
               /|\  |
                |   |
                   ===
            """,
            """
                +---+
                O   |
               /|\  |
                |   |
               /   ===
            """,
            """
                +---+
                O   |
               /|\  |
                |   |
               / \ ===
            """
        ]

        # Başlangıçta zoruk seviyesi ve ipucu ayarları
        self.zorluk_seviyesi = 'Kolay'
        self.ipucu_aktif = False

        self.kelime = ''
        self.tahmin = []
        self.hak = 6

        self.düzen = QHBoxLayout()
        self.sol_düzen = QVBoxLayout()

        self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
        self.kelime_etiket.setFont(QFont('Arial', 24))
        self.sol_düzen.addWidget(self.kelime_etiket)

        self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
        self.hak_etiket.setFont(QFont('Arial', 14))
        self.sol_düzen.addWidget(self.hak_etiket)

        # Zorluk seviyesi seçim kutusu
        self.zorluk_seviyesi_kutusu = QComboBox(self)
        self.zorluk_seviyesi_kutusu.addItems(['Kolay', 'Orta', 'Zor'])
        self.zorluk_seviyesi_kutusu.setCurrentText(self.zorluk_seviyesi)
        self.zorluk_seviyesi_kutusu.currentTextChanged.connect(self.zorluk_seviyesi_degistir)
        self.sol_düzen.addWidget(self.zorluk_seviyesi_kutusu)

        # İpucu butonu
        self.ipucu_butonu = QPushButton('İpucu Al', self)
        self.ipucu_butonu.clicked.connect(self.ipucu_al)
        self.sol_düzen.addWidget(self.ipucu_butonu)

        # Harf tahmini için giriş alanı ve buton
        self.harf_girişi = QLineEdit(self)
        self.harf_girişi.setPlaceholderText('Harf giriniz...')
        self.sol_düzen.addWidget(self.harf_girişi)

        self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
        self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
        self.sol_düzen.addWidget(self.harf_tahmin_butonu)

        # Kelime tahmini için giriş alanı ve buton
        self.kelime_girişi = QLineEdit(self)
        self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
        self.sol_düzen.addWidget(self.kelime_girişi)

        self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
        self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
        self.sol_düzen.addWidget(self.kelime_tahmin_butonu)

        # Yeni oyun ve çıkış butonları
        self.buton_düzeni = QHBoxLayout()

        self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
        self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
        self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

        self.çıkış_butonu = QPushButton('Çıkış', self)
        self.çıkış_butonu.clicked.connect(self.close)
        self.buton_düzeni.addWidget(self.çıkış_butonu)

        self.sol_düzen.addLayout(self.buton_düzeni)

        self.ascii_etiket = QLabel(self)
        self.ascii_etiket.setFont(QFont('Courier', 18))
        self.ascii_etiket.setText(self.ascii_stages[0])

        self.düzen.addLayout(self.sol_düzen)
        self.düzen.addWidget(self.ascii_etiket)
        
        self.setLayout(self.düzen)
        self.yeni_oyun()

    def zorluk_seviyesi_degistir(self, yeni_seviye):
        self.zorluk_seviyesi = yeni_seviye
        self.yeni_oyun()

    def ipucu_al(self):
        if self.ipucu_aktif:
            QMessageBox.information(self, 'İpucu', 'İpucu zaten kullanıldı.')
            return

        for i, karakter in enumerate(self.kelime):
            if self.tahmin[i] == '_':
                self.tahmin[i] = karakter
                break

        self.kelime_etiket.setText(' '.join(self.tahmin))
        self.ipucu_aktif = True

        if '_' not in self.tahmin:
            self.oyun_sonu(True)
        else:
            QMessageBox.information(self, 'İpucu', f'İpucu: {karakter} harfini buldunuz!')

    def harf_tahmini(self):
        harf = self.harf_girişi.text().upper()
        self.harf_girişi.clear()

        if len(harf) != 1 or not harf.isalpha():
            QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
            return

        if harf in self.kelime:
            if harf in self.tahmin:
                QMessageBox.warning(self, 'Hata', 'Bu harfi zaten tahmin ettiniz.')
                return

            for i, karakter in enumerate(self.kelime):
                if karakter == harf:
                    self.tahmin[i] = harf

            self.kelime_etiket.setText(' '.join(self.tahmin))

            if '_' not in self.tahmin:
                self.oyun_sonu(True)
        else:
            self.hak -= 1
            self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
            self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

            if self.hak == 0:
                self.oyun_sonu(False)

    def kelime_tahmini(self):
        kelime = self.kelime_girişi.text().upper()
        self.kelime_girişi.clear()

        if kelime == self.kelime:
            self.tahmin = list(self.kelime)
            self.kelime_etiket.setText(' '.join(self.tahmin))
            self.oyun_sonu(True)
        else:
            self.hak -= 1
            self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
            self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

            if self.hak == 0:
                self.oyun_sonu(False)

    def oyun_sonu(self, kazandi):
        if kazandi:
            QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')
        else:
            QMessageBox.warning(self, 'Kaybettiniz', f'Hakkınız bitti, kelime: {self.kelime}')
        self.yeni_oyun()

    def yeni_oyun(self):
        self.kelime = choice(self.kelimeler[self.zorluk_seviyesi]).upper()
        self.tahmin = ['_'] * len(self.kelime)
        self.hak = 6
        self.ipucu_aktif = False
        self.kelime_etiket.setText(' '.join(self.tahmin))
        self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
        self.ascii_etiket.setText(self.ascii_stages[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    oyun = WordGuessingGame()
    oyun.show()
    sys.exit(app.exec_())