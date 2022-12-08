10.#osa
from math import *
print("Ajate")
v=float(input("sisesta aja minutitus")
t=int(v//60)
sec=int(v%60)
print(f"minutes {t} sec {sec}")




9.#osa
from math import *
("uiskude kogukiirus on 29-9 km/h")
v=24.4/60
t=v*29.9
t=round(t,2)
print(f"Vestlus {t}km")
print()

8.#osa
from math import *
print("Kütusekulu arvutamine")
l=float(input("Kasutaja sisestab tangitud kütuse liitrid"))
km=float(input("Kasutaja sisestab läbitud kilomeetrid"))
p=l/km*100 
print (str(f"Vastus: {p}l/km"))
print()






7.#osa
from math import *
print("pitsa hinnaga 12,90€ jätate teenindajale 10% jootraha")
s=10*12.90/100
s=round(s)
d=(12.90+s)
print(f"Vastus: {d}")
p=d/3
p=round(p,1)
print (f"iga lollpea peab:{p}")

6.#osa
from math import *
from random import *
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")

5.#osa
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("   ^^ "" ^^ " )

4.#osa
from math import *
print("aritmeetilise keskmise arvutamine.")
a=int(input("1arv: "))
b=int(input("2arv: "))
c=int(input("3arv: "))
d=int(input("4arv: "))
e=int(input("5arv: "))
S=((a+b+c+d+e)/5)
print(f"Vastus: {S}")




3.#osa
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print()
print("Sinu kiirus oli " + str(round(kiirus)) + "km/h")




2.#osa
from math import *
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} n**2")




1.#osa
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt"))
d=2*(C/(2*pi))
print(f"Vastus :\nPuu Läbimõõduga {C} ümbermõõt võrdub {d}")