class Lekarz:

    def __init__(self, _imie, _nazwisko, _specjalizacja, _plec, _placa, _oddzial):
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.specjalizacja = _specjalizacja
        self.plec = _plec
        self.placa = _placa
        self.oddzial = _oddzial

    def __str__(self):
        s = "imie: " + self.imie + "\n"
        s += "nazwisko: " + self.nazwisko + "\n"
        s += "specjalizacja: " + self.specjalizacja + "\n"

        if self.plec == "k":
            s += "plec: Kobieta \n"
        else:
            s += "plec: Mezczyzna \n"

        s += "pensja: " + self.placa + "\n"
        s += "oddzial: " + self.oddzial + "\n"

        return s


class Pracownicy:
    def __init__(self):
        self.listaLekarzy = list()

    def __str__(self):
        s = ""
        for l in self.listaLekarzy:
            s +=  l.__str__() + "\n"

        return s