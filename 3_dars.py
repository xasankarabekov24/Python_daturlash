#Xasan Karabekov 26.10.2022

#3-dars STRING(MATN)

#STRING (matn) — Pythondagi eng mashxur ma'lumot turlaridan biri.
#o'zgaruvchiga matn yuklash uchun matn qo'shtirnoq (" ") yoki birtirnoq (' ')
#ichida yozilishi kerak.


viloyat = "Жиззах" #o`zgaruvchining qiymati istalgan tilda yozilishi mumkin
tuman = "Фориш"
print(viloyat)
print(tuman)


#Pythonda matnlar Unicode(https://unicode-table.com/en/) jadvalidagi
#istalgan belgilardan iborat bo`lishi mumkin,( o`zbek,arab,hind,xitoy
#alifbosidagiharflar yoki turli emoji-smayliklar)


#MATNLARNI QO`SHISH OPERATORI

#Matnlarni qo`shish uchun matimatik amal (+) amalidan foydalanamiz

ism = "Xasan"                 #bu yerda (ism) o`zgaruvchi 
print("Mening ismim" + ism)   # "Mening ismim" matn (+)qo`shish operatori


ism = "Muhammad"    #Natija: MuhammadAxmedov bu kodda ism va familya 
familya = "Axmedov" #orasiga bo`shliq belgisini qo`shmaganimiz uchun ikki matn
print(ism + familya)# qo`shilib yozildi. Bu xatoni to`g`rilash uchun
# 3 chinchi qatorni quyidagicha yozamiz
ism = "Muhammad"
familya = "Axmedov"
print(ism + ' ' + familya) #(' ') ikki o`zgaruvchini orasidagi bo`sh joy qo`yish


#f"{}"-string

#ikki va undan ko`p matn ko`rinishidagi o`zgaruvchilarni birlashtirish uchun
#f"{}"-string usulidan f"{matn1} {matn2}" ko`rinishida ham yozishimiz mumkin.

ism = "Xasan"
familya = "Karabekov"
ism_sharif = f"{ism} {familya}"
print(ism_sharif)               #Natija: Xasan Karabekov

#f"{matn}"-usuli yordamida uzun matnlarni ham yasash mumkin.
ism = "Xasan"
familya = "Karabekov"
print(f"Salom, mening ismim:{familya}. {ism} {familya}")#Natija: Karabekov.Xasan Karabekov

#Pythonda maxsus belgilar
# Matnga bo`shliq qo`shish uchun (\t) belgisidan
#Yangi qatordan boshlash uchun(\n) belgisidan foydalanamiz

print('Hello world')# oddiy matn
print('Hello \tWorld')# Matnda bo`shliq
print('Hello \nWorld')# Matnni yangi qatordan boshlash


#String Metodlari
#Pythona string ustida amalga oshirishmumkin bo`lgan tayyor amallar
# to`plami mavjud Bunday amallar metodlar deyiladi.

#Metodlarni qo`llash uchun metod nomini matndan so`ng .metod_nomi()
#ko`rinishida yoziladi.

# BAZI METODLAR BILAN TANISHAMIZ

#upper() metodi matndagi har bir harfni katta harfga o`zgartiradi 
ism = "Xasan"
familya = "Karabekov"
ism_sharif = f"{ism} {familya}"
print(ism_sharif.upper())       #Natija: XASAN KARABEKOV

#lower()-metodi upper() metodining aksi har bir harfni kichik harga o`zgartiradi
ism = "Xasan"
familya = "Karabekov"
ism_sharif = f"{ism} {familya}"
print(ism_sharif.lower())  #Natija: xasan karabekov

#title()-metodi faqat eng birinchi so`zning bosh harfini katta bilan yozadi
ism = "Xasan"
familya = "Karabekov"
ism_sharif = f"{ism} {familya}"
print(ism_sharif.title())

#capitalize()esa faqat eng birinchi so`zning birinchi harfini katta bilan yozadi
# bu metod faqat so`zning birinchi so`zning birinchi harfini kattaga o`zgartiradi.
#ikkinchi keladingan so`zga esa tasir eta olmaydi.
ism = "Xasan"
familya = "Karabekov"
ism_sharif = f"{ism} {familya}"
print(ism_sharif.capitalize())


#O`zgaruvchilarni faqat o`zgaruvchilarga emas, balki to`g`ridan to`g`ri matnga ham
#qo`llash mumkin(aslida o`zgaruvchilar ham matinning (yoki boshqa ma`lumotning
#)manzili xolos)
print('XasanKarabekov'.upper())#Natija o`sha o`sha XasanKarabekov


# strip(),rstrip() va lstrip()metodlari
#bu metodlar matining boshi va oxiridagi bo`sh joylarni olib tashlaydi.
#1.lstrip()- matn boshidagi bo`shliqni olib tashlaydi
#2.rstrip()- matn oxiridagi bo`shliqni olib tashlaydi.
#3. strip()-matn boshi va oxridagi bo`shliqni olib tashlaydi

dastur = "    Python    "
print("Men" + dastur.lstrip() + "dasturlash tilini o`rganmoqchiman")
print("Men" + dastur.rstrip() + "dasturlash tilini o`rganmoqchiman")
print("Men" + dastur.strip() + "dasturlash tilini o`rganmoqchiman")

#Metodlar o`zgaruvchi ichidagi asl matnni o`zgartirmaydi

#Input-foydalanuvchi bilan uloqot
#Biz o`zgaruvchilarning qiymatini dasturning ichida beryotgan edik. Endi qiymatni
#o`zimiz emas balki dastur foydalnuvchilariga kiritish imkonini beramiz
#Buning uchun input()-funksiyasidan foydalanamiz

ism = input("Ismingiz nima?")    #Natija: Ismingiz nima Xasan
print("Assalom alaykum, " + ism) #Assalom alykum, Xasan

#Kodni yanada chiroyli ko`rinishi uchun yuqoridagi o`rgangan ba`zi bir medodlardan
#foydalanamiz
ism = input("Ismingiz nima?\n>>>")
print("Assalom alaykum, " + ism.title())



    #Amaliyot

#Quyidagi mashqlarni bajaring:

#1.Quyidagi o'zgaruvchilarni yarating:
#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#2.Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini
#foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
#3.Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
#4.Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.











