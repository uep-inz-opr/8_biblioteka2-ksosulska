class Biblioteka:
    def __init__(self):
        self.limit_wypozyczen = 3
        self.egzemplarze = []
        self.ksiazki = []
        self.czytelnicy = {}

    def dodaj(self, tytul, autor, rok_wydania):
        ksiazka = Ksiazka(tytul, autor)
        egzemplarz = Egzemplarz(ksiazka, rok_wydania)

        self.egzemplarze.append(egzemplarz)

        for k in self.ksiazki:
            if k.tytul == tytul and k.autor == autor:
                k.liczba += 1
                return True
        
        self.ksiazki.append(ksiazka)
        return True

    def wypozycz(self, nazwisko_czytelnika, tytul):
        try:
            czytelnik = self.czytelnicy[nazwisko_czytelnika]
        except KeyError:
            czytelnik = Czytelnik(nazwisko_czytelnika)
            self.czytelnicy[nazwisko_czytelnika] = czytelnik

        if len(czytelnik.egzemplarze) == self.limit_wypozyczen:
            return False

        if tytul in czytelnik.egzemplarze:
            return False
        else:
            for egzemplarz in self.egzemplarze:
                if egzemplarz.ksiazka.tytul == tytul:
                    if egzemplarz.wypozyczony:
                        continue
                    else:
                        egzemplarz.wypozyczony = True
                        czytelnik.egzemplarze[tytul] = egzemplarz
                        return True
            return False

    def oddaj(self, czytelnik, tytul):
    
        pass


class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        self.liczba = 1

    def __repr__(self):
        return repr((self.tytul, self.autor, self.liczba))


class Egzemplarz:
    def __init__(self, ksiazka, rok_wydania):
        self.ksiazka = ksiazka
        self.rok_wydania = rok_wydania
        self.wypozyczony = False

    def __repr__(self):
        return repr((self.ksiazka.tytul, self.ksiazka.autor, self.rok_wydania))


class Czytelnik:
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko
        self.egzemplarze = {}


b = Biblioteka()

n = int(input()[1:3])

for i in range(0, n):
    k = eval(input())
    akcja = k[0]

    if akcja == 'dodaj':
        print(b.dodaj(k[1], k[2], k[3]))
    elif akcja == 'wypozycz':
        print(b.wypozycz(k[1], k[2]))
    elif akcja == 'oddaj':
        print(b.oddaj(k[1], k[2]))
