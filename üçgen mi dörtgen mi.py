import time
while True:
    secim=str(input("\nüçgen mi dörtgen mi (çıkış:'q'): "))
    if(secim=='q'):
        print("programdan çıkılıyor...")
        time.sleep(0.3)
        break
    elif((secim=="dörtgen") or (secim=="dortgen")):
        print("Dört kenar giriniz:\n")
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        if(a==b==c==d):
            print("kare")
        elif((a==b and c==d) or (a==c and b==d) or (a==d and b==c)):
            print("dikdörtgen")
        else:
            print("sıradan dörtgen")
            
    elif((secim=="üçgen") or (secim=="ücgen") or (secim=="uçgen") or (secim=="ucgen")):
        print("üç kenar giriniz:\n")
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        if(a==b==c):
            print("eşkenar")
        elif((a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b)):
            print("ikizkenar")
        elif((a<(b+c) and a>abs(b-c)) or (b<(a+c) and b>abs(a-c)) or (c<(a+b) and c>abs(a-b))):
            print("sıradan bir üçgen")
        else:
            print("üçgen belirtmiyor")
    else:
        print("hatalı giriş yaptınız:")
