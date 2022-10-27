'''dizi=[]
sayı1 = input()
sayı2 = input()
sayı3 = input()
sayı4 = input()
sayı5 = input() 
dizi=[sayı1,sayı2,sayı3,sayı4,sayı5]
for x in dizi:
    x = x*x-20

    for x in dizi:
        print(x)'''




import enum
import re
from tkinter import N


dizi = []
for i in range (0, 5):
    dizi.append(int(input()))


def siralama_fonk(a):
    return a*a-20

dizi.sort(key=siralama_fonk)
print(dizi)


a= 5
c= 4
d=-5

if a > c:
    print("a c den büyük")

if d < 0: print("d o dan küçük")

if d > 0 : print("asdad"); print("sdfsaa"); d=5


a=5
if a > 5:
    print("a 5 ten büyük")
elif a == 5:
    print("a 5 e eşit")
else:
    print("a 5 ten küçük")


a = 5
b = 4
print("a ile b farklı") if a != b else print("a ile b aynı")



if a < 10 or c < 10:
    print("a ya da b 10 dan küçüktür")

if a == 5 or c == 10:
    print("a 5 e eşit ve c 10 a eşittir")


a = 4
c = 11
if c <5:
    if c > 10:
        print("merhaba dünya")

if a > 5:
    pass
print("sfsdfs")


a = 5
while a < 15:
    a += 1
    if a == 8:
        continue
    if a == 12:
        break
else:
    print("a artık 15 ya da daha büyük")

for i in range (0, 10):
    print(i)

for i in range (0, 10, 2):
    print(i)

for i in range (10, 0, -2):
    print(i)

liste = ["as", True, ".9, 5, "["ssd","sdsad","sfds"]]

for i, eleman in enumerate(liste):
    print(i+1, ". eleman :", eleman, sep="")

def yazdir():
    print("yazıyorum")

yazdir()


def topla(a, b):
   return a+b

print(topla(3,5))



def topla_carp(a, b):
   return a+b,a*b

print(topla_carp(3,5))

toplam, carpim = topla_carp(3, 5)
print(topla_carp(3,5))
print(toplam, carpim)


def topla_ne_varsa_git(*a):
    toplam=0
    for deger in a:
        toplam += a
    return toplam

    print(topla_ne_varsa_git(3,5,9,15.2,36))

def topla(*toplanacak, fazladan =0):
 toplam =0
 for deger in toplanacak:
        toplam += deger + fazladan
 return toplam

print(topla(3,5,9,15.2,36, fazladan =2, file= "a.txt"))


def birim_islem(**birim):
    print("birim adı :" + birim["ad"])
    print("birim Tipi :" + birim["tip"])
    print("birim yılı :" + birim["yil"])

birim_islem(ad="balıkesir", tip="üniversite", yil=1992)


lambda_fonksiyonu = lambda a:a+10

print(lambda_fonksiyonu(5))


cok_parametre = lambda a,b: a+b
print(topla(3,5))

"""ha bu sınavda çıkar"""
def benim_fonksiyonum(n):
    return lambda a: a*n

katini_al = benim_fonksiyonum(2)
print(katini_al(5))

katini_al = benim_fonksiyonum(5)
print(katini_al(5))

