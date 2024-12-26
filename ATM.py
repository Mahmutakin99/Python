print('''
işlemler;
1)Bakiye sorgulama
2)para yatırma
3)para çekme
çıkmak için 'q'ya basınız
''')
bakiye=1000

while True:
    işlem=input("işlem seçiniz:")
    if(işlem == 'q'):
        print("sistemden çıkılıyor")
        break
    elif(işlem=="1"):
        print("bakiye sorgulanıyor:")
        print("bakiyeniz {}₺ dir".format(bakiye))
    elif(işlem=="2"):
        a=float(input("yatırılacak tutarı giriniz:"))
        bakiye+=a
        print("işlem sonu bakiyeniz {}₺ dir".format(bakiye))
    else:
        print("bakiyeniz {}₺ dir çekeceğiniz tutar bakiyenizi aşamaz!".format(bakiye))
        a=float(input("çekilecek tutarı giriniz"))
        if(a>bakiye):
            print("girilen tutar bakiyeyi aştığı için işlem yapılamadı:")
            continue
        elif(a==bakiye):
            print("bakiyenizin hepsi çekiliyor:")
            bakiye-=a
            print("işlem tamamlandı işlem sonu bakiye {}₺ dir".format(bakiye))
        else:
            bakiye-=a
            print("işlem tamamlandı işlem sonu bakiye {}₺ dir".format(bakiye))
            