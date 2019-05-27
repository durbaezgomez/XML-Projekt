from xml.dom import minidom, NotFoundErr
from pracownicy import *

doc = minidom.parse("projekt.xml")

def getValFromElemByTag(element, tag):
    return str(element.getElementsByTagName(tag)[0].firstChild.data)


def getValFromAttrByTag(element, tag):
    return str(element.getAttribute(tag))


def getLekarze():

    for lekarz in lekarze:
        imie = getValFromElemByTag(lekarz, "imie")
        nazwisko = getValFromElemByTag(lekarz, "nazwisko")
        specjalizacja = getValFromElemByTag(lekarz, "specjalizacja")
        plec = getValFromAttrByTag(lekarz, "plec")
        placa = getValFromAttrByTag(lekarz, "placa")
        oddzial = getValFromAttrByTag(lekarz, "oddzial")
        pr.listaLekarzy.append(Lekarz(imie, nazwisko, specjalizacja, plec, placa, oddzial))

def poprawnoscPolityczna():
    try:
        for l in lekarze:
            l.removeAttribute("plec")
    except NotFoundErr:
        print("No such attribute in this element!")

def zmienNaStanDobry():
    try:
        stacjo = sprzet.getElementsByTagName("komputery")[0].getElementsByTagName("stacjonarne")[0].getElementsByTagName("produkt")
        laptopy = sprzet.getElementsByTagName("komputery")[0].getElementsByTagName("laptopy")[0].getElementsByTagName("produkt")

        for s in stacjo:
            if s.hasAttribute("stan"):
                s.setAttribute("stan", "dobry")

        for l in laptopy:
            if l.hasAttribute("stan"):
                l.setAttribute("stan", "zly")

    except NotFoundErr:
        print("No such attribute in this element!")

def dodajPacjenta(_imie, _nazwisko, _wiek, _choroba):
    nowy = pacjenci[0].cloneNode(deep=True)
    choroba = doc.createElement("choroba")

    chorobaText = doc.createTextNode(_choroba)
    choroba.appendChild(chorobaText)
    nowy.appendChild(choroba)

    nowy.insertBefore(doc.createComment("NOWY PACJENT"),nowy.getElementsByTagName("imie")[0])

    nowy.getElementsByTagName("imie")[0].firstChild.nodeValue = _imie
    nowy.getElementsByTagName("nazwisko")[0].firstChild.nodeValue = _nazwisko
    nowy.getElementsByTagName("wiek")[0].firstChild.nodeValue = _wiek
    szpital.getElementsByTagName("pacjenci")[0].appendChild(nowy)

def usunPacjenta(_nazwisko):
    for p in pacjenci:
        if p.getElementsByTagName("nazwisko")[0].firstChild.data == _nazwisko:
            szpital.getElementsByTagName("pacjenci")[0].removeChild(p)

def ilePacjentow():
    if szpital.getElementsByTagName("pacjenci")[0].hasChildNodes():
        return pacjenci.length


szpital = doc.getElementsByTagName("szpital")[0]
pracownicy = szpital.getElementsByTagName("pracownicy")[0]
lekarze = pracownicy.getElementsByTagName("lekarze")[0].getElementsByTagName("lekarz")
pielegniarki = pracownicy.getElementsByTagName("pielegniarki")[0].getElementsByTagName("pielegniarka")
pacjenci = szpital.getElementsByTagName("pacjenci")[0].getElementsByTagName("pacjent")
sprzet = szpital.getElementsByTagName("sprzet")[0]


pr = Pracownicy()
getLekarze()
print pr

poprawnoscPolityczna()
zmienNaStanDobry()
dodajPacjenta("Nowy", "Pacjent", 45, "Straszne Chorobsko")
usunPacjenta("Kozak")



print "W SZPITALU JEST " + str(ilePacjentow()) + " PACJENTOW"
with open("parsedXML.xml", "w") as xml_file:
    doc.writexml(xml_file)






