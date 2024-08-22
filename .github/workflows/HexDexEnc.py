#Encode ve Decode
import time

#oncelikle girdi alalim

rakam = int(input("Rakamı Girin:  "))
cevirici = (hex(rakam))
time.sleep(1)
print(f"Hex: {cevirici}")

def hexi_donustur():
   hexj = input("Hex Kodunuzu yaziniz: ")
   donustur = int(hexj, 16)
   time.sleep(1)
   print(f"Gercek Rakam: {donustur}")
   
while True:
   try:
      soru = input("Hex Decode etmek istiyormusunuz (e\h): ")
      if soru == "e":
         time.sleep(1)
         hexi_donustur()
         time.sleep(1)
      elif soru == "h":
         break

   except:
      print("Hata")
