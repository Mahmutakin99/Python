#   Blackjack Game
import random,sys,os

# Terminal penceresini İşletim sistemine göre temizler
def clear_terminal():
  if sys.platform.startswith('win'):
    os.system('cls')
  else:
    os.system('clear')

# Oyun Başındaki Görsel
img = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
      |  \/ K|                            _/ |                
      '------'                           |__/           

'''

# Sürekli tekrar eden kart alma kodlarını kısaltmak için
def kartal(oyuncuKart):
  As = None
  kartlar = [As,2,3,4,5,6,7,8,9,10,10,10,10]
  Okart = random.choice(kartlar)
  if Okart == As:
    ch = input("As kartı geldi hangi değeri seçmek istrersiniz (1 veya 11)")
    if ch == '1':
      Okart = 1
    else:
      Okart = 11
  oyuncuKart.append(Okart)

# As kartı geldiğinde onun değerini belirler
def AsKartı(As,oyuncuKart,bilgisayarKart):
  if As:
    ch = input("As kartı geldi hangi değeri seçmek istrersiniz (1 veya 11): ")
    if ch == '1':
      Okart = 1
    else:
      Okart = 11
    oyuncuKart.append(Okart)
  else:
    if sum(bilgisayarKart) > (21/2):
      bkart = 1
    else:
      bkart = 11
    bilgisayarKart.append(bkart)

# Kartlar toplamı kontrol edilerek oyunun bitmesini sağlar
def OyunDurumu(oyuncuKart,bilgisayarKart,img):
  if sum(oyuncuKart) > 21:
    print("oyuncu kaybetti")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
      clear_terminal()
      sys.exit()
    else:
      clear_terminal()
      oyun(img)
  
  elif sum(bilgisayarKart) > 21:
    print("oyuncu kazandı")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
      clear_terminal()
      sys.exit()
    else:
      clear_terminal()
      oyun(img)
      
  elif sum(oyuncuKart) < sum(bilgisayarKart):
    print("oyuncu kaybetti")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
      clear_terminal()
      sys.exit()
    else:
      clear_terminal()
      oyun(img)
      
  elif sum(oyuncuKart) > sum(bilgisayarKart):
    print("oyuncu kazandı")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
      clear_terminal()
      sys.exit()
    else:
      clear_terminal()
      oyun(img)
  elif sum(oyuncuKart) == sum(bilgisayarKart):
    print("berabere kazanan yok")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
          clear_terminal()
          sys.exit()
    else:
          clear_terminal()
          oyun(img)

# BlacJack durumu yani kartlar toplamı 21 olup olmama durumu kontrol eder
def BlackJack(oyuncuKart,bilgisayarKart):
  if sum(oyuncuKart) == 21:
    print("!!BlackJack!! oyuncu kazandı")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
      clear_terminal()
      sys.exit()
    else:
      clear_terminal()
      oyun(img)
          
  if sum(bilgisayarKart) == 21:
    print("!!BlackJack!! Oyuncu kaybetti")
    ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
    if ch3 == 'n':
      clear_terminal()
      sys.exit()
    else:
      clear_terminal()
      oyun(img)

# Sonsuz döngülerle uğraşmamak için oyunu kendini tekrar tekrar çağıran bir fonksiyon olarak oluşturuldu
def oyun(img):
  print(img)
  # As kartının değerini sonradan vereceğimiz için değerini None yapıyoruz
  As = None
  # Kartların değerini tutan liste
  kartlar = [As,2,3,4,5,6,7,8,9,10,10,10,10]
  # oyunu başlatmak veya kapatmak için seçim noktası
  choice = input("oynamak için y çıkmak için n ye basınız:\n--> ")
  if choice == 'n':
    # Terminal penceresini temizleme
    clear_terminal()
    # Programı sonlandırma
    sys.exit()
  
  # Boş kart listeleri
  oyuncuKart = []
  bilgisayarKart = []
  
  for _ in range(2):
    # bir listeden random kart seçmek için random kütüphanesinden choice fonksiyonu kullanılır
    Okart = random.choice(kartlar)
    # Kartın as olma durumu kontrol edilir
    if Okart == As:
      As = True
      AsKartı(As,oyuncuKart,bilgisayarKart)
    #   ch = input("As kartı geldi hangi değeri seçmek istrersiniz (1 veya 11)")
    #   if ch == '1':
    #     Okart = 1
    #   else:
    #     Okart = 11
    # oyuncuKart.append(Okart)
    
    # Kart as değilse olduğu gibi listeye eklenir
    else:
      oyuncuKart.append(Okart)
  
  
  bkart = random.choice(kartlar)
  if bkart == As:
    As = False
    AsKartı(As = As, oyuncuKart = oyuncuKart, bilgisayarKart = bilgisayarKart)
  #   if sum(bilgisayarKart) < (21//2):
  #     bkart = 11
  #   else:
  #     bkart = 1
  # bilgisayarKart.append(bkart)
  else:
    bilgisayarKart.append(bkart)
  
  print(f"İlk kartlar:\nOyuncu kartları {oyuncuKart} Kartlar toplamı: {sum(oyuncuKart)}\nBilgisayar kartları {bilgisayarKart} Kartlar toplamı: {sum(bilgisayarKart)}")
  BlackJack(oyuncuKart=oyuncuKart,bilgisayarKart=bilgisayarKart)
  
  # Oyun başladıktan sonra kart almaya devam etmeyene kadar devamlı kart almak için sonsuz döngü oluşturulur
  kartAl = True
  while kartAl:
    ch2 = input("kart almak istermisiniz(evet y yada hayır n): ")
    if ch2 == 'n':
      bkart = random.choice(kartlar)
      if bkart == As:
        AsKartı(As = As, oyuncuKart = oyuncuKart, bilgisayarKart = bilgisayarKart)
      #   if bilgisayarKart == None:
      #     bilgisayarKart = 0
      #   if sum(bilgisayarKart) < (21/2):
      #     As = 11
      #   else:
      #     As = 1
      # bilgisayarKart.append(bkart)
      # print(f"kartlar:\nOyuncu kartları: {oyuncuKart}\nBilgisayar kartları: {bilgisayarKart}")
      else:
        bilgisayarKart.append(bkart)
        
      print(f"kartlar:\nOyuncu kartları: {oyuncuKart} Kartlar toplamı: {sum(oyuncuKart)}\nBilgisayar kartları: {bilgisayarKart} Kartlar toplamı: {sum(bilgisayarKart)}")
      # BlackJack olma durumu kontrol edilmek için kartlar fonksiyona gönderilir
      BlackJack(oyuncuKart=oyuncuKart,bilgisayarKart=bilgisayarKart)
      # Bilgisayarın elindeki kartlar toplamı 17 den küçükse 17 yi geçene kadar kart alması sağlanır
      if sum(bilgisayarKart) < 17:
        devam = True
        while devam:
          bkart = random.choice(kartlar)
          if bkart == As:
            AsKartı(As = As, oyuncuKart = oyuncuKart, bilgisayarKart = bilgisayarKart)
          #   if bilgisayarKart == None:
          #     bilgisayarKart = 0
          #   if sum(bilgisayarKart) < (21/2):
          #     As = 11
          #   else:
          #     As = 1
          # bilgisayarKart.append(bkart)
          else:
            bilgisayarKart.append(bkart)
            
          print(f"kartlar:\nOyuncu kartları: {oyuncuKart} Kartlar toplamı: {sum(oyuncuKart)}\nBilgisayar kartları: {bilgisayarKart} Kartlar toplamı: {sum(bilgisayarKart)}")
          BlackJack(oyuncuKart=oyuncuKart,bilgisayarKart=bilgisayarKart)
          
          if sum(bilgisayarKart) > 17:
            devam = False
        print(f"kartlar:\nOyuncu kartları: {oyuncuKart} Kartlar toplamı: {sum(oyuncuKart)}\nBilgisayar kartları: {bilgisayarKart} Kartlar toplamı: {sum(bilgisayarKart)}")
      # Oyunun bittiğini kontrol etmek için kartlar fonksiyona gönderilir
      OyunDurumu(oyuncuKart=oyuncuKart,bilgisayarKart=bilgisayarKart,img=img)
      # if sum(oyuncuKart) > 21:
      #   print("oyuncu kaybetti")
      #   ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
      #   if ch3 == 'n':
      #     sys.exit()
      #   else:
      #     print("\n"*20)
      #     oyun(img)
      
      # elif sum(bilgisayarKart) > 21:
      #   print("oyuncu kazandı")
      #   ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
      #   if ch3 == 'n':
      #     sys.exit()
      #   else:
      #     print("\n"*20)
      #     oyun(img)
      
      # elif sum(oyuncuKart) < sum(bilgisayarKart):
      #   print("oyuncu kaybetti")
      #   ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
      #   if ch3 == 'n':
      #     sys.exit()
      #   else:
      #     print("\n"*20)
      #     oyun(img)
      
      # elif sum(oyuncuKart) > sum(bilgisayarKart):
      #   print("oyuncu kazandı")
      #   ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
      #   if ch3 == 'n':
      #     sys.exit()
      #   else:
      #     print("\n"*20)
      #     oyun(img)

    else:
      kartal(oyuncuKart)
      print(f"kartlar:\nOyuncu kartları: {oyuncuKart} Kartlar toplamı: {sum(oyuncuKart)}\nBilgisayar kartları: {bilgisayarKart} Kartlar toplamı: {sum(bilgisayarKart)}")
      BlackJack(oyuncuKart=oyuncuKart,bilgisayarKart=bilgisayarKart)
      # if sum(oyuncuKart) == 21:
      #   print("!!BlackJack!! oyuncu kazandı")
      #   ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
      #   if ch3 == 'n':
      #     sys.exit()
      #   else:
      #     print("\n"*20)
      #     oyun(img)
      # if sum(bilgisayarKart) == 21:
      #   print("!!BlackJack!! Oyuncu kaybetti")
      #   ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
      #   if ch3 == 'n':
      #     sys.exit()
      #   else:
      #     print("\n"*20)
      #     oyun(img)
      
      # kartlar toplamı 21 i geçerse oyun doğrudan sonlanır
      if sum(oyuncuKart) > 21:
        print("oyuncu kaybetti")
        ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
        if ch3 == 'n':
          clear_terminal()
          sys.exit()
        else:
          clear_terminal()
          oyun(img)
      if sum(bilgisayarKart) > 21:
        print("oyuncu kazandı")
        ch3 = input("yeni oyuna geçilsin mi evet y yada hayır n: ")
        if ch3 == 'n':
          clear_terminal()
          sys.exit()
        else:
          clear_terminal()
          oyun(img)

# Oyunu çağırıyoruz
oyun(img)