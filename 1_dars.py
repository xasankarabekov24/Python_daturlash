# Xasan Karabekov 24.10.2022

                 #Print sintex va arifmetik amallar



print("Asslomu alaykum") # bu bizning birinchi ko`dimiz F5ni bosib RUN qilamiz
                         # Natija konsolga Asslomu alaykum matni chiqadi


print(Xayrli kun!)# Bu safar Syntax Error: invalid syntax xatolik xabarini chiqardi
                  # print() funksiyasi matn yoki ifodalarni konsolga chiqarish vazifalarini
                  #bajaradi Lekun ushbu funksiya ishlashi uchun bir nechta qoidalarga amal
                  # qilish lozim. Agar matnimizni konsolga chiqarmoqchi bo`lsak qo`shtirnoq
                  #(" ") yoki (' ') birtirnoq orasida yozishimiz kerak.
print('Xayrli kun!')# to`g`ri yozilgan kod

print("Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami")# Yuoqridagi matnni birtirnoq orqali
                                                                      #ham konsolga chiqarish mumkinmi? Matndagi yo'q,
                                                                      #g'am so'zlaridagi birtirnoqlar bunga to'sqinlik qilmaydimi?
                                                                      #Qiladi. Buning oldini olish uchun esa matndagi birtirnoq
                                                                      #belgisidan avval \ belgisini qo'yish lozim


print('Odami ersang, demagil odami, \nOniki, yo\'q xalq g\'amidin g\'ami')# Yuqoridagi kodga e'tibor bergan bo'lsangiz yo'q so'zi yo\'q
                                                                          #ko'rinishida g'am so'zi esa g\'am ko'rinishida yozilgan. Umuman
                                                                          #olganda \ belgisi har qanday mahsus belgi oldidan qo'yiladi.

                                                                          #Agar yuqordagi kodimizda \ belgisini ishlatmaganimizda natija qanday bo'lar edi?


print('Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami')  #SyntaxError: invalid syntax
                                                                        #Keling shu o'rinda Syntax Error (sinteksda xatolik) haqida ham gaplashaylik.

                           # SINTEKS XATOLIK
#Har bir tilda orfografik va grammatik qoidalar bo'lgani kabi, dasturlash tillarining ham o'ziga yarasha qonun-qoidalari bor.
#Bu qoidalar to'plami sinteks (syntax) deb ataladi. Sinteks xatolik (Syntax Error) deb esa shu qoidalarning buzilishiga aytiladi.

#Misol uchun keraksiz joyda qo'yilgan nuqta, vergul yoki bo'sh joy, shuningdek ma'lum funktsiyalar nomini xato yozish (print()
#o'rniga prit()), ochilmay yoki yopilmay qolgan qavs, noo'rin bo'shliq, qolib ketgan kalit so'z (keyword) kabilar ham Syntax Error hisoblanadi.
#Syntax Error eng ko'p uchraydigan xatolik bo'lib, Python bunday xatolik bor dasturlarni bajarmaydi.      


                        #ARIFMETIK AMALLAR




#print() funktsiyasi nafaqat matn, balki turli ifodalarni ham konsolga chiqaradi.
      
print(2+4*2)# Pyton arifmetik amallarni bajarishda matimatik qoidalarga amal qiladi.
            #Qavs ichidagi ammalar qavs ortidagilardan avval bajariladi.
            #Darajaga oshirish (Ildiz chiqarish)ko`paytirish va bo`1ishdan avval bajariladi
            #Ko`paytirish va bo`lish, qo`shish va ayrishdan avval bajariladi
            #Boshqa holatlarda ifodalar chapdan o`nga qarab bajariladi
print(2+4*2)# Bu misolda ham avval ko`paytirish (4*2=8), keyin esa qo`shish
            #amali (2+8=10) bajariladi.

print(20/5)# / belgisi bo`lish amalini bajaradi va natijada har doim o`nlik son
           #ko`rinishida bo`ladi. Natija 4.0


#Bo`lish amalidan butun son olish uchun (//) lik bo`lish amalidan foydalanamiz
print(16//4)#Natija 4
print(10//3)#Natija 3


print(2**4) #(**)belgisi darajaga oshirishni anglatadi, yani 2**4 ifodafi 2 ning
             # 4-darajasini beradi. Natija 16


#print() yordamida matn ifodalarni jamlab chiqarish mumin, Buning uchun har bir
# ifoda va matinni vergul(,)bilan ajratiladi.
print("To`qqiznning kvadrati",9**2, "ga teng")#Natija To`qqiznning kvadrati 81 ga teng

print('3x3=', 3*3) #Natija 3x3=9

    #Izohlar (Comments)


# Yaxshi dasturchilarning odatlaridan biri har qanday kodni izohlar bilan tushuntirib ketish.
#Izohlar kelajakda o'zimiz uchun ham, boshqalar uchun ham dasturimiz qanday ishlashini tushunishda yordam beradi.     

      
#Radiusi 5 ga teng bo'lgan aylananing uzunligi quyidagicha hisoblanadi
print(2*5*3.14159)



#Yuqoridagi misolda # belgisidan keyin yozilgan matn izoh (comment) deyiladi.
#Izoh alohida qatorda yoki qator oxiridan ham yozilishi mumkin. Python # dan keyingi har qanday matnni
#(qator oxirigacha) e'tiborsiz qoldiaradi. # dan keyin yozligan kodlar ham bajarilmaydi:      
      
print("Assalom alaykum!") # Bu matn konsolda chiqadi
#Keyingi qator esa bajarilmaydi
#print("Mening ismim Xasan")

      #AMALIYOT
#Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:

#"Nexia", "Tico", 'Damas' ko'rganlar qilar havas

#Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:

#5 ning 4-darajasini toping
#22 ni 4 ga bo'lganda qancha qoldiq qoladi?
#Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
