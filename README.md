# XML-Projekt
Dominik Urbaez Gomez

## XML WYMAGANIA
### Przykładowy element
```xml
<pacjent plec='m' oddzial='Choroby Wewnetrzne'>
			<imie>Jerzy</imie>
			<nazwisko>Nowak</nazwisko>
			<wiek>67</wiek>
			<leki>
				<lek>
					<nazwa>Buderin</nazwa>
					<dawka>3 x 1 tabletka</dawka>
				</lek>
				<lek>
					<nazwa>Filytol</nazwa>
					<dawka>1 x 1 tabletka</dawka>
				</lek>
			</leki>
		</pacjent>
```
## CSS WYMAGANIA - ZAJĘCIA
### 1. display, 2. padding, 3. border, 4. margin 
```css
lekarz, pielegniarka, pacjent,produkt{
	display: block;
	padding: 3px;
	border: solid #a2a8d3;
	margin: 4px;
	background-color: #FDCEA2
}
```
### 5.before
```css
lekarze:before{
	content: "LEKARZE:";
}
```
### 6. font-size
```css
nazwisko, nazwa, model, specjalizacja{
	font-size: 15px;
	font-weight: bold; 
}
```
### 7. kolor
```css
specjalizacja{
	color: #a2a8d3;
}
```
### 8. text decoration
```css
imie, nazwisko, model{
	text-decoration: underline;
}
```
### 9. hover
```css
lekarze:hover, pielegniarki:hover, pacjenci:hover, diagnostyka:hover, chirurgia:hover, komputery:hover{
	background: red;
}
```
## CSS WYMAGANIA - POZA ZAJĘCIAMI 
### 1. liczenie wierszy
```css
lekarze{
	counter-reset: lek;
}
lekarz:before{
	counter-increment: lek;
	content: counter(lek);
}
```
### 2 - cienie, 3 - gradienty
```css
lekarze, pielegniarki, pacjenci, diagnostyka, chirurgia, komputery{

	display: inline;
	float: left;
	width: 30%;
	border: solid #a2a8d3;
	margin: 6px;
	filter: drop-shadow(-1px 6px 3px rgba(50, 50, 0, 0.5));
	transition: background 0.5s ease-out;
	-webkit-transition: background-color 2s ease-out;
 	-moz-transition: background-color 2s ease-out;
	-o-transition: background-color 2s ease-out;
  	transition: all 2s ease-out;
	background-image: linear-gradient(72deg,#ffa952, #feffdf);
}
```
### 4.hover transition
```css
nazwisko:hover, specjalizacja:hover{
    color:#f00;
    transition: all 0.5s ease;
}
```
## DTD WYMAGANIA


## XSD WYMAGANIA

## XSLT WYMAGANIA

## DOM WYMAGANIA
