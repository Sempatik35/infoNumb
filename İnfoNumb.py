import phonenumbers
from phonenumbers import timezone
from phonenumbers import carrier




print("""
                            .   
o      ,-                   |   
. ;-.  |  ,-. ;-. . . ;-.-. |-. 
| | |  |- | | | | | | | | | | | 
' ' '  |  `-' ' ' `-` ' ' ' `-' 
      -'                        
     
      """)

print("""                            
             Created By SEMPATİK       
         ╚────────────────────────────╝
      """)



no = input("Hedef Numarayı Alan Kodu İle  Giriniz : ") 

print(" ")

from phonenumbers import geocoder
number = phonenumbers.parse(no)
print("────────Ulke────────────────")  
print(geocoder.description_for_number(number,'tr'))
print("────────────────────────────")  

print(" ")
print(" ")

number = phonenumbers.parse(no)
print("────────Lokasyon────────────") 
print(timezone.time_zones_for_number(number))
print("────────────────────────────") 

print(" ")
print(" ")

print("────────Operator────────────") 
number = phonenumbers.parse(no)
print(carrier.name_for_number(number, 'tr'))
print("────────────────────────────") 

print(" ")
print(" ")