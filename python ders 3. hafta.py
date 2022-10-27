def polindrom(*dram):
   toplam = fark = 0
   for sayi in dram:
    if str(sayi)[::-1]==(str(sayi)):
        toplam += sayi
    else:
        fark += sayi
   return toplam - fark 
    

print(polindrom(10,101,55,40,9009))
    
class sinif:
     a=5
     b= "asdsasdd"
     c = [1,4,6]

     def yazdir(self):
        d = 100
        print(d, self.a)

     def yazdir2(self, t):
        print(t) 


nesne = sinif()
print(nesne.a)
nesne.yazdir2(876765)
nesne.a=999
print(nesne.a)



class sinif:
    def __init__(self,a):
       self.metin =a
    def __del__(self):
        print("beni siliyorlar...")

    def __str__(self):
        return "yazdırılan :" + self.metin
    

nesne = sinif("Metin")
print(nesne.metin)


def topla(a,b):
    return a+b
def carp(a,b):
    return a*b

q=5
w="asd"
e = [2,3,5]

# module import
 
import bizim_modul

print(bizim_modul.topla(5,10))
print(bizim_modul.e)

print(topla(2,3))

print(bm.q)


x = "asda"
try:
   y= 5 + x
except:
    print("'int' and 'str'")  


    import os

    dosya =open("ders3.txt,'r'")

    for satir in dosya:
        print(satir[:-1])

    dosya = open("cop.txt",'w')

    print("köylüler", file =dosya)

    dosya.close()