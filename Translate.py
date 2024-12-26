# from googletrans import Translator


# # function that translates the entered text using google translate
# def translateText(text, targetLang):
#   translator = Translator()
#   Translation = translator.translate(text, dest = targetLang)
#   return Translation.text

# while True:
    
#     select=int(input("**********************************\n1 to start/continue processing Press 0 to stop/finish.\nProcess selection: "))
#     if(select==0):
#         select2=str(input("you have chosen to stop the transaction, should the transaction be executed? 'yes' or 'no'\nWhat's your choice: "))
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
    
#     # text to translate
#     text = input("\ntext to translate: ")

#     # target language choice
#     targetLang = input("1) Turkish\n2) English\n3) German\n4) Spanish\n5) Japanese\n6) French\n7) Russian\n\nEnter the code for a language in: ")

#     if targetLang == '1':
#         targetLang = "tr"
#     elif targetLang == '2':
#         targetLang = "en"
#     elif targetLang == '3':
#         targetLang = "de"
#     elif targetLang == '4':
#         targetLang = "es"
#     elif targetLang == '5':
#         targetLang = "ja"
#     elif targetLang == '6':
#         targetLang = "fr"
#     elif targetLang == '7':
#         targetLang = "ru"
#     else: # To prevent possible errors
#         print("An incorrect selection code please correct.")

#     # text translation
#     TranslatedText = translateText(text, targetLang)

#     # Çevrilen metni ekrana yazdır
#     print(f"**********************************\n({text}) when translated into the desired language --> {TranslatedText}")


# from PyQt5 import QtWidgets, QtGui
# from googletrans import Translator
# import sys

# class TranslatorApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()
    
#     def initUI(self):
#         self.setWindowTitle('Çeviri Uygulaması')
#         self.setGeometry(100, 100, 400, 300)

#         self.layout = QtWidgets.QVBoxLayout()
        
#         self.textEdit = QtWidgets.QTextEdit(self)
#         self.layout.addWidget(self.textEdit)

#         self.comboBox = QtWidgets.QComboBox(self)
#         self.comboBox.addItem("Türkçe", "tr")
#         self.comboBox.addItem("İngilizce", "en")
#         self.comboBox.addItem("Almanca", "de")
#         self.comboBox.addItem("İspanyolca", "es")
#         self.comboBox.addItem("Japonca", "ja")
#         self.comboBox.addItem("Fransızca", "fr")
#         self.comboBox.addItem("Rusça", "ru")
#         self.layout.addWidget(self.comboBox)

#         self.translateButton = QtWidgets.QPushButton('Çevir', self)
#         self.translateButton.clicked.connect(self.translateText)
#         self.layout.addWidget(self.translateButton)

#         self.resultLabel = QtWidgets.QLabel(self)
#         self.layout.addWidget(self.resultLabel)

#         self.setLayout(self.layout)
    
#     def translateText(self):
#         text = self.textEdit.toPlainText()
#         targetLang = self.comboBox.currentData()
        
#         if text.strip() == "":
#             self.resultLabel.setText("Çevrilecek metni giriniz.")
#             return
        
#         translator = Translator()
#         translation = translator.translate(text, dest=targetLang)
#         self.resultLabel.setText(translation.text)

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     translatorApp = TranslatorApp()
#     translatorApp.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()



from PyQt5 import QtWidgets, QtGui, QtCore
from googletrans import Translator
import sys

class TranslatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Çeviri Uygulaması')
        self.setGeometry(100, 100, 600, 500)

        # Main layout
        layout = QtWidgets.QVBoxLayout()

        # Title
        title = QtWidgets.QLabel("Çeviri Uygulaması", self)
        title.setFont(QtGui.QFont('Arial', 20, QtGui.QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        # Input text
        input_layout = QtWidgets.QVBoxLayout()
        input_label = QtWidgets.QLabel("Çevirmek İstediğiniz Metni Girin:", self)
        input_label.setFont(QtGui.QFont('Arial', 12))
        input_layout.addWidget(input_label)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setPlaceholderText("Metni buraya girin...")
        self.textEdit.setFont(QtGui.QFont('Arial', 12))
        input_layout.addWidget(self.textEdit)

        layout.addLayout(input_layout)

        # Language selection
        langLayout = QtWidgets.QHBoxLayout()
        langLabel = QtWidgets.QLabel("Hedef Dil: ", self)
        langLabel.setFont(QtGui.QFont('Arial', 12))
        langLayout.addWidget(langLabel)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setFont(QtGui.QFont('Arial', 12))
        self.comboBox.addItem("Türkçe", "tr")
        self.comboBox.addItem("İngilizce", "en")
        self.comboBox.addItem("Almanca", "de")
        self.comboBox.addItem("İspanyolca", "es")
        self.comboBox.addItem("Japonca", "ja")
        self.comboBox.addItem("Fransızca", "fr")
        self.comboBox.addItem("Rusça", "ru")
        langLayout.addWidget(self.comboBox)

        layout.addLayout(langLayout)

        # Translate button
        self.translateButton = QtWidgets.QPushButton('Çevir', self)
        self.translateButton.setFont(QtGui.QFont('Arial', 12))
        self.translateButton.clicked.connect(self.translateText)
        layout.addWidget(self.translateButton)
        
        self.exitButton = QtWidgets.QPushButton('Çıkış', self)
        self.exitButton.setFont(QtGui.QFont('Arial', 12))
        self.exitButton.clicked.connect(QtWidgets.qApp.quit)
        layout.addWidget(self.exitButton)

        # Output text
        output_layout = QtWidgets.QVBoxLayout()
        output_label = QtWidgets.QLabel("Çevrilen Metin:", self)
        output_label.setFont(QtGui.QFont('Arial', 12))
        output_layout.addWidget(output_label)

        self.resultTextEdit = QtWidgets.QTextEdit(self)
        self.resultTextEdit.setFont(QtGui.QFont('Arial', 12))
        self.resultTextEdit.setReadOnly(True)
        output_layout.addWidget(self.resultTextEdit)

        layout.addLayout(output_layout)

        self.setLayout(layout)
    
    def translateText(self):
        text = self.textEdit.toPlainText()
        targetLang = self.comboBox.currentData()
        
        if text.strip() == "":
            self.resultTextEdit.setText("Çevrilecek metni giriniz.")
            return
        
        translator = Translator()
        translation = translator.translate(text, dest=targetLang)
        self.resultTextEdit.setText(translation.text)
        self.textEdit.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    translatorApp = TranslatorApp()
    translatorApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

