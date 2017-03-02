import math

class vektor(object):
    def __init__(self, *args):
        # ustvari vektor
        # zapisan mora biti kot a=vektor(x1,x2,...)
        self.vrednost = args
    
    def __add__(self, other):
        # sesteje z + v tuple
        # a je stevilo v prvem vektorju, b je stevilo v drugem vektorju

        seznam = [0 for i in range(max(self.dimenzija(), other.dimenzija()))]       # ustvari seznam dolzine daljsega vektorja

        for i, x in enumerate(self):        # vrednosti iz obeh vektorjev sesteje v seznam v seznam
            seznam[i] += x
        for i, x in enumerate(other):
            seznam[i] += x

        sestej = tuple(seznam)
        return vektor(*sestej)      # vrne vsoto vektorjev

    def __sub__(self, other):
        # racunanje z -
        # odstej = tuple(a-b for a,b in zip(self, other))
        odstej = self + (-1 * other)
        return odstej

    def __mul__(self, other):
        # racunanje z *
        # tu se stvari zapletejo, ker imajo vektorji 3 razlicne razlage za *
        # zato jih moram lociti z if
        if type(other) == type(self):
            # to bi moralo delovati za navadno mnozenje in skalarni produkt
            zmnozi = sum(tuple(a*b for a,b in zip(self, other)))
            return zmnozi # tu ni vektor(*zmnozi), ker zmnozi v tem primeru ni vektor ampak skalar
        else:
            # mnozenje s skalarjem (dela SAMO ce je najprej vektor ((1,2,3)*5))
            zmnozi = tuple([i*other for i in self])
            return vektor(*zmnozi)

    def __rmul__(self, other):
        # obrne vrstni red vektorja in skalarja, in izvede zgornjo funkcijo
        # izvede se, v primeru, ko je skalar pred vektorjem (4*(1,2,3))
        return self.__mul__(other)

    def __truediv__(self, other):
        # definira deljenje vektorja s skalarjem
        # ne bo delovalo v obratnem vrstnem redu, ker nismo definirali deljenja skalarja z vektorjem
        # ne bo delovalo z dvema vektorjema, ker tudi to ni definirano
        try:
            deli = tuple([i/other for i in self])
            return vektor(*deli)
        except ZeroDivisionError:
            raise ZeroDivisionError("Napaka: deljenje z 0")

    def __eq__(self, other):
        return self.vrednost==other.vrednost
    
    def __iter__(self):
        # omogoca zapisovanje inputa
        return self.vrednost.__iter__()
    
    def __repr__(self):
        return str(self.vrednost)

    def __str__(self):
        return str(self.vrednost)      

    def dolzina(self):
        # formula: koren(a1^2+a2^2+a3^2+...)
        # ta funkcija uporabi funkcijo za skalarni produkt vektorjev
        # kar zmanjsa kolicino kode
        # kodo je potrebno zapisati kot a.dolzina() (a je vnesen vektor)
        dolzinaVektorja = math.sqrt(self*self)
        return dolzinaVektorja
        
    def dimenzija(self):
        # izracun dimenzije vektorja
        # vrne dimenzijo vektorja
        # kodo je potrebo zapisati kot a.dimenzija() (a je vnesen vektor)
        dimension = len(self.vrednost)
        return dimension

    def polarniZapis(self):
        r = self.dolzina()      # dolzina vektorja
        if(self.dimenzija()<=1):
            return vektor(r)
        elif(self.dimenzija()==2):
            # formula: "r"=(r,f)
            # print(r) #za preverjanje
            f = vektor.vmesniKot(self, vektor(1))       # izracun  kota
            polarniZapisVektorja = vektor(r,f)
            return polarniZapisVektorja
        elif(self.dimenzija()==3):
            x = self*(vektor(1))
            y = self*(vektor(0,1))
            z = self*(vektor(0,0,1))
            f = vektor.vmesniKot(vektor(x,y), vektor(1))    # izracun kota med projekcijo in x osjo
            cilindricniZapisVektorja = vektor(r,f,z)        
            return cilindricniZapisVektorja
        else:
            raise ValueError("Napaka: dimenzija vektorja je prevelika.")

    @staticmethod
    def vmesniKot(a, b):
        # formula: cos(f)=(a*b)/(|a|*|b|)
        # rezultat je kot med vektorjema
        # kot bo v stopinjah
        # zapis v programu: vektor.vmesniKot(a,b)
        kot = round(math.degrees(math.acos(round((a * b) / (a.dolzina() * b.dolzina()), 5))), 5)
        return kot

    def kolinearnost(a, b):
        # izracuna kot med vektorjema, ce je enak 180 ali 0 stopinj, to pomeni da sta vektorja kolinearna
        kot = vektor.vmesniKot(a,b)
        # return kot # za preverjanje
        if (kot == 0 or kot == 180):
            return True
        else:
            return False