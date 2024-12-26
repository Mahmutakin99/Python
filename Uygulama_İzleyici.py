# import time
# import subprocess

# def is_app_running(app_name):
#     try:
#         output = subprocess.check_output(['osascript', '-e', f'tell application "System Events" to (name of processes) contains "{app_name}"'])
#         return 'true' in output.decode('utf-8').lower()
#     except subprocess.CalledProcessError:
#         return False

# def track_application(application_path):
#     app_name = application_path.split('/')[-1].replace('.app', '')
    
#     # Uygulamayı başlat
#     subprocess.Popen(["open", application_path])
#     start_time = time.time()

#     print(f"{application_path} uygulaması başlatıldı...")

#     try:
#         # Uygulamanın çalışıp çalışmadığını kontrol et
#         while is_app_running(app_name):
#             time.sleep(1)

#     except KeyboardInterrupt:
#         print("Uygulama izleme işlemi kesildi.")
    
#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     print(f"{application_path} uygulamasında geçirilen süre: {elapsed_time:.2f} saniye")

# if __name__ == "__main__":
#     application_path = input("İzlemek istediğiniz uygulamanın tam yolunu girin: ")
#     track_application(application_path)

# /System/Applications/Music.app

import sys
import time
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

def is_app_running(app_name):
    try:
        output = subprocess.check_output(['osascript', '-e', f'tell application "System Events" to (name of processes) contains "{app_name}"'])
        return 'true' in output.decode('utf-8').lower()
    except subprocess.CalledProcessError:
        return False

class AppTracker(QThread):
    elapsed_time_signal = pyqtSignal(float)

    def __init__(self, app_path):
        super().__init__()
        self.app_path = app_path
        self.app_name = app_path.split('/')[-1].replace('.app', '')

    def run(self):
        start_time = time.time()
        subprocess.Popen(["open", self.app_path])
        
        while is_app_running(self.app_name):
            time.sleep(1)

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.elapsed_time_signal.emit(elapsed_time)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Uygulama İzleyici')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('İzlemek istediğiniz uygulamanın tam yolunu girin:', self)
        layout.addWidget(self.label)

        self.app_path_input = QLineEdit(self)
        layout.addWidget(self.app_path_input)

        self.start_button = QPushButton('Başlat', self)
        self.start_button.clicked.connect(self.start_tracking)
        layout.addWidget(self.start_button)
        
        self.exit_button = QPushButton('Çıkış',self)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)
        
        self.setLayout(layout)

    def start_tracking(self):
        app_path = self.app_path_input.text()
        if app_path:
            self.tracker = AppTracker(app_path)
            self.tracker.elapsed_time_signal.connect(self.show_elapsed_time)
            self.tracker.start()

    def show_elapsed_time(self, elapsed_time):
        dakika = int(elapsed_time/60)
        saniye = elapsed_time - (dakika * 60)
        QMessageBox.information(self, "Uygulama Süresi", f"Uygulamada geçirilen süre: {dakika} dakika ve {saniye:.2f} saniyedir.")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())