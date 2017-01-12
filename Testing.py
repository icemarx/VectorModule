from Vektor3 import *

#test purposes only
l = vektor(1,42)
m = vektor(1,2,3)
n = vektor(1,1,1)

print(11+3)
print(m+n)
print(m+l)
print(m-n)
print(m-l)
print(m*n)
print(m*2)
print(3*m)
print(5*4)
print(20/5)
print(19/5)
print(m/5)
print(m/0)
print(m==n)
print(m==m)
print(m==vektor(1,2,3))
print(m.dolzina())
print(n.dolzina())
print(m.dolzina()+n.dolzina())
print(l.polarniZapis())
print(m.polarniZapis())
print(vektor.vmesniKot(m,n))
print(kolinearnost(m,n))
print(vektor.vmesniKot(m,m))
print(kolinearnost(m,m))

test = (42+((m/4+n).dolzina())/5)*(m*(1.0/2))
print (test)

#ideje:
			#prevedi v python 3 (NARJENO (python3 -i Kalkulator.py))
			#stevilo dimenzij vektorja (NAREJENO)
			# definirej == (NARJENO)
			#sestej/odstej vektor v n dimenzijah z vektorjem v n+m dimenzijah (NAREJENO)
	#polarni zapis vektorja v n dimenzijah
#izracun vektorja med dvema tockama
#python documentacija (help)

#v poročilu napisi uvod, kaj je python, kaj so moduli,...

#https://docs.python.org/2/library/operator.html
#http://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-in-python-division-keeps-rounding
#https://docs.python.org/2.7/tutorial/errors.html
