import os

def mukemmelSayiBul():           # Klasik olarak fonksiyonlari yerlestirdim.
    while secim:
        girilenSayi = int(input("Mukemmel sayi mi?: "))

        bolenToplami = 0

        for i in range(1, girilenSayi):             # 1 ile girilecek sayi arasindaki tum sayilar
            if (girilenSayi % i == 0):              # Eger girilen sayi 1 ile arasindaki sayilara bolunebiliyorsa ve kalan 0
                bolenToplami += i                   # ise bolenToplami degiskenine o sayiyi ekle. 

        if bolenToplami == girilenSayi:
            print("Bu sayi bir mukemmel sayidir.!!")            
            input("Cikmak icin bir tusa basin!")
            os.system('cls | | clear')
            break
        elif bolenToplami != girilenSayi:
            print("Degildir")
            input("Cikmak icin bir tusa basin!")
            break
            os.system('cls | | clear')      # Cikmak icin bir tusa bastiracagiz ve 
                                                             # Terminali temizletecegiz.

def TamBolenleriBul():
    while secim:                                                                              
        girilenSayi = int(input("Tam bolenlerini bulmak istedigin sayiyi giriniz: "))

        bolenler = []                              
        for i in range(1, girilenSayi):             # Bos bir bolenler listesi tanimladim ve 1 ile girilen sayi
            if (girilenSayi % i == 0):              # arasindaki tum sayilari girilen sayiya boldurmeye calistim.
                bolenler.append(i)                  # Eger kalansiz bolunuyorsa, kalansiz bolunen sayilari bos listeye ekle!

        print(f"Tam bolenlerin listesi = {bolenler}")
        if bolenler == [1]:                                       # Eger ortak bolen sadece 1 ise. Bu asal sayidir.
            print("Asal sayi secmissin reyis")                    # Birde kendisine bolunebiliyor zaten. Onu saymiyoruz bile
            input("Cikmak icin bir tusa basiniz")
            break
            os.system('cls | | clear')

            
def AsalMiBu():
    while secim:
        girilenSayi = int(input("Asal sayi olup olmadigini bulmak istediginiz sayiyi giriniz: "))

        for sayilar in range(2, girilenSayi):
            if girilenSayi % sayilar == 0:                 # Girilen sayi 2 ile kendisine kadar olan sayilara bolununce
                                                           # Kalan eger 0 ise Asal Sayi degildir.
                print("Senin Sayi asal degil.")
                input("Cikmak icin bir tusa basin!")
                break
                os.system('cls | | clear')
                
            else:                                                         
                print("Senin sayi asal cikti.")
                input("Cikmak icin bir tusa basin!")
                break
                os.system('cls | | clear')
                
        break

def ArmstrgonMuBu():
    num = int(input("Armstrong sayi olup olmadigini bilmek istedigin sayiyi gir: "))
    toplam = 0
    gecici = num                                              # Armstrong Sayinin ne oldugunu ogrenmek icin
    while gecici > 0:                                         # http://matkafasi.com/42198/armstrong-sayi
        basamak = gecici % 10
        toplam += basamak ** 3                                # Basamak sayisini ogreniyoruz. Ve toplam degiskenine
        gecici //= 10                                         # basamakla 3 u carparak degiskene ekliyoruz.

    if num == sum:
        print(num, "bir Armstrong sayidir")
        input("Cikmak icin bir tusa basin")
        os.system('cls | | clear')
    else:
        print(num, "bir Armstrong sayi degildir")
        input("Cikmak icin bir tusa basin!")
        os.system('cls | | clear')

def SayiyiYaziyaCevir():
    birler = ["","Bir","Iki","Uc","Dort","Bes","Alti","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kirk","Elli","Altmis","Yetmis","Seksen","Doksan"]
    
    def okunus(sayi):
        birinci = sayi % 10                                     # Onlar Basamagi
        ikinci = sayi // 10                                     # Birler Basamagi

        return onlar[ikinci] + " " + birler[birinci]

    sayi = int(input("Sayi: "))
    print(okunus(sayi))


def CarpimTablosu():
    for i in range(1,11):
        print("***************************************************************")
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}")                           # Dongu icinde dongu kullanarak her seferinde
    input("Cikmak icin bir tusa basin!")                          # Donen iki degisken elde ettik.
    os.system('cls | | clear')


while 1:

    print("""
[1] Mukemmel Sayiyi Bul
[2] Sayinin Tam Bolenlerini Bul
[3] Sayi Asal Sayi Mi Bul
[4] Armstrong Sayi Mi Bul
[5] Yazacagin Sayiyi Yaziya Cevir
[6] 1 den 10'a kadar olan sayilari Carpim Tablosuna Bastir

    """)
    secim = int(input("Bir secim giriniz: "))

    if secim == 1:
        mukemmelSayiBul()
    elif secim == 2:
        TamBolenleriBul()
    elif secim == 3:
        AsalMiBu()
    elif secim == 4:
        ArmstrgonMuBu()
    elif secim == 5:
        SayiyiYaziyaCevir()
    elif secim == 6:
        CarpimTablosu()
        
    else:
        print("Programdan cikiliyor...")
        quit()
        os.system('cls' if os.name == 'nt' else 'clear')
