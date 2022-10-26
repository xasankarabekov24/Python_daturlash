#Xasan Karabekov 26.10.2022
#3-Dars javoblar

#1.Quyidagi o'zgaruvchilarni yarating:
#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
kocha = "Bog`bon"
mahalla = "Sog`bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha  + ' ''kochasi,', mahalla  +' '"mahallasi,", tuman + ' ' "tumani,", viloyat + ' ' "viloyati")

#2.Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini
#foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha = input("Ko`changizni kiriting?")
mahalla = input("Mahallangizni kiriting?")
tuman = input("tumanigizni kiriting?")
viloyat = input("viloyatingizni kiriting?")
print(kocha  + ' ''kochasi,', mahalla  +' '"mahallasi,", tuman + ' ' "tumani,", viloyat + ' ' "viloyati")

#3.Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
kocha = "Bog`bon"
mahalla = "Sog`bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")
#4.Yuqoridagi matnni f-string yordamida, yangi, manzil
#deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida
#o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
kocha = "Nurafshon"
mahalla = "O`zbekiston"
tuman = "Forish"
viloyat = "Jizzax"
manzil = f"{kocha} kochasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati"
print(manzil)
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())


