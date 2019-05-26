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
## DTD WYMAGANIA - WŁASNOŚCI ELEMENTÓW
### 1. jeden element
```
<!ELEMENT sprzet (rodzaje)>
```
### 2. jeden lub wiecej elementow
```
<!ELEMENT leki (lek+)>
```
### 3. zero lub wiecej elementow
```
<!ELEMENT lekarze (lekarz)*>
```
### 4. jeden lub zero elementow
```
<!ELEMENT lek (nazwa, dawka?)>
```
### 5. wartość typu #PCDATA
```
<!ELEMENT imie (%pcd;)>
```
### 6. wartość spośród dwóch opcji
```
<![IGNORE[  <!ELEMENT pracownicy ((lekarze, pielegniarki) | (inni))*> ]]>
```
## DTD WYMAGANIA - WŁASNOŚCI ATRYBUTÓW
### 1. atrybut opcjonalny
```
<!ATTLIST produkt stan %cd; %imp;>
```
### 2. atrybut wymagany
```
<!ATTLIST lekarz oddzial %cd; %rq;>
```
### 3. atrybut z domyślną wartością
```
<!ATTLIST produkt stan %cd; #FIXED 'dobry'>
```
### 4. atrybut z wartością dowolną z podanych
```
<!ATTLIST lekarz plec (m|k) %rq;>
```
### 5. atrybut, gdzie wartosc to jedno slowo
```
<!ATTLIST produkt producent NMTOKEN %rq;>
```
### 6. atrybut, gdzie wartość może składać się z wielu słów
```
<!ATTLIST pielegniarka oddzial NMTOKENS %rq;>
```
## DTD WYMAGANIA - ENCJE PARAMETRYCZNE WEWNĘTRZNE I SEKCJA WARUNKOWA
### 1. CDATA
```
<!ENTITY % cd "CDATA">
```
### 2. #REQUIRED
```
<!ENTITY % rq "#REQUIRED">
```
### 3. sekcja warunkowa
```
<![INCLUDE[ <!ELEMENT pracownicy (lekarze, pielegniarki)*> ]]>
<![IGNORE[  <!ELEMENT pracownicy ((lekarze, pielegniarki) | (inni))*> ]]>
```
## XSD WYMAGANIA - WŁASNOŚCI TYPÓW
### 1. pattern
```xml
<xs:simpleType name="oddzialType2">
  	<xs:restriction base="xs:string">
    	<xs:pattern value="ODZ[0-9]{3}"/>
	</xs:restriction>   
</xs:simpleType>
```
### 2. min/max Length
```xml
<xs:simpleType name="oddzialType">
    <xs:restriction base="xs:string">
      <xs:minLength value="5"/>
      <xs:maxLength value="50"/>
    </xs:restriction>
  </xs:simpleType>
```
### 3. enumeration
```xml
<xs:simpleType name="plecType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="k"/>
      <xs:enumeration value="m"/>
    </xs:restriction>
  </xs:simpleType>
```
### 4. list
```xml
<xs:simpleType name="oddzialyType">
    <xs:list itemType="oddzialType"/>
 </xs:simpleType>
```
### 5. maxOccurs
```xml
<xs:complexType name="lekarzeType">
    <xs:sequence>
      <xs:element type="lekarzType" name="lekarz" maxOccurs="unbounded" minOccurs="0"/>
    </xs:sequence>
</xs:complexType>
```
### 6. use required
```xml
<xs:attribute type="plecType" name="placa" use="required"/>
```
### 7. min/max Inclusive
```xml
<xs:simpleType name="stazType">
    <xs:restriction base="xs:integer">
      <xs:minInclusive value="0"/>
      <xs:maxInclusive value="50"/>
    </xs:restriction>
</xs:simpleType>
```
### 8. mix/max Exclusive
```xml
<xs:simpleType name="wiekType">
    <xs:restriction base="xs:unsignedInt">
      <xs:minExclusive value="0"/>
      <xs:maxExclusive value="120"/>
    </xs:restriction>
  </xs:simpleType>
```
### 9. minOccurs
```xml
<xs:complexType name="lekarzeType">
    <xs:sequence>
      <xs:element type="lekarzType" name="lekarz" maxOccurs="unbounded" minOccurs="0"/>
    </xs:sequence>
</xs:complexType>
```
### 10. default attribute value
```xml
<xs:attribute type="oddzialyType" name="oddzial" default="Ogolny"/>
```
### 11. fixed attribute value
```xml
<xs:attribute type="xs:string" name="stan" fixed="dobry"/>
```
### 12. optional attribute use
```xml
<xs:attribute type="plecType" name="plec" use="optional"/>
```
### 13. group elements
```xml
<xs:group name="imieNazw">
    <xs:sequence>
      <xs:element name="imie" type="xs:string"/>
      <xs:element name="nazwisko" type="xs:string"/>
    </xs:sequence>
  </xs:group>
```
### 14. union memberTypes
```xml
<xs:simpleType name="oddzialType">
  	<xs:union memberTypes="oddzialType1 oddzialType2"/>
</xs:simpleType>
```
### 15.  totalDigits
```xml
<xs:simpleType name="placaType">
    <xs:restriction base="xs:integer">
      <xs:totalDigits value="5"/>
    </xs:restriction>
  </xs:simpleType>
```
### 16. restriction length
```xml
<xs:simpleType name="godzinyPracyType">
    <xs:restriction base="xs:string">
      <xs:length value="11"/>
    </xs:restriction>
  </xs:simpleType>
```
### 17. all
```xml
<xs:complexType name="rodzajeType">
    <xs:all>
      <xs:element type="diagnostykaType" name="diagnostyka"/>
      <xs:element type="chirurgiaType" name="chirurgia"/>
      <xs:element type="komputeryType" name="komputery"/>
    </xs:all>
  </xs:complexType>
```
### 18.  choice
```xml
<xs:complexType name="pracownicyType">
  	<xs:choice>
  		<xs:sequence>
	      <xs:element type="lekarzeType" name="lekarze"/>
	      <xs:element type="pielegniarkiType" name="pielegniarki"/>
    	</xs:sequence>
    	<xs:sequence>
    		<xs:element type="pracownicyType" name="pracownicy"/>
    	</xs:sequence>
  	</xs:choice>
  </xs:complexType>
```
## XSD WYMAGANIA - TYPY WBUDOWANE
### 1. string
```xml
<xs:element name="imie" type="xs:string"/>
```
### 2. integer
```xml
<xs:simpleType name="stazType">
    <xs:restriction base="xs:integer">
      <xs:minInclusive value="0"/>
      <xs:maxInclusive value="50"/>
    </xs:restriction>
</xs:simpleType>
```
### 3. boolean
```xml
<xs:attribute type="xs:boolean" name="nadgodziny" use="required"/>
```
### 4. positiveInteger
```xml
<xs:element name="rocznik" type="xs:positiveInteger"/> 
```
### 5. float
```xml
<xs:element name="dawka" type="xs:float"/>
```
### 6.unsigned Int
```
<xs:simpleType name="wiekType">
    <xs:restriction base="xs:unsignedInt">
      <xs:minExclusive value="0"/>
      <xs:maxExclusive value="120"/>
    </xs:restriction>
  </xs:simpleType>
```
## XSLT WYMAGANIA - WYKORZYSTANIE RÓŻNORODNYCH ELEMENTÓW
### 1. for-each, 2. select
```html
<td>
	<b><xsl:text>Wynagrodzenia lekarzy: </xsl:text></b>
</td>
<td>
	<xsl:for-each select="pracownicy/lekarze/lekarz">
		<xsl:value-of select="substring(@placa,0,5)"/>
		<xsl:text> PLN</xsl:text>
		<br/>
	</xsl:for-each>
</td>
```
### 3. sort, 4. choose
```html
<td>
	<xsl:for-each select="pracownicy/lekarze/lekarz">
		<xsl:sort select="@placa" order="descending"/>
			<xsl:choose>
			  <xsl:when test="@plec='k'">
			    <p class="women">
			      <xsl:value-of select="imie "/>
			      <xsl:text> </xsl:text>
			      <xsl:value-of select="nazwisko"/>
			    </p>
			  </xsl:when>

			  <xsl:otherwise>
			    <p class="men">
			      <xsl:value-of select="imie "/>
			      <xsl:text> </xsl:text>
			      <xsl:value-of select="nazwisko"/>
			    </p>
			  </xsl:otherwise>
			</xsl:choose>
	</xsl:for-each>
</td>
```
### 5.if
```html
<td>
	<xsl:for-each select="pracownicy/lekarze/lekarz">
		<xsl:if test="substring(@placa,0,5) > 4000">
		  <xsl:value-of select="@placa"/>
		  <br/>
		</xsl:if>
	</xsl:for-each>
</td>
```
### 6. comment
```html
<xsl:comment>
	To jest opis danych dotyczących szpitala zawartych w pliku xml.
</xsl:comment>
```
### 7. text
```html
<td>
	<b><xsl:text>Ilość lekarzy</xsl:text></b> 
</td>
```
### 8. call-template
```html
<td>
	<xsl:call-template name="zarobki"/>
</td>
```
## XSLT WYMAGANIA - FUNKCJE I WYRAŻENIA xPATH
### 1. count()
```html
<tr>
	<td>
		<b><xsl:text>Ilość lekarzy</xsl:text></b> 
	</td>
	<td>
		<xsl:value-of select="count(pracownicy/lekarze/lekarz)"/>
	</td>
</tr>
```
### 2.sum()
```html
<td>
	<b><xsl:text>Średnia wieku wszystkich pacjentów: </xsl:text></b>
</td>
<td>
	<xsl:value-of select="sum(pacjenci/pacjent/wiek) div count(pacjenci/pacjent)"/>
</td>
```
### 3. substring()
```html
<td>
	<b><xsl:text>Wynagrodzenia lekarzy: </xsl:text></b>
</td>
<td>
	<xsl:for-each select="pracownicy/lekarze/lekarz">
		<xsl:value-of select="substring(@placa,0,5)"/>
		<xsl:text> PLN</xsl:text>
		<br/>
	</xsl:for-each>
</td>
```
### 4.concat()
```html
<td>
	<b><xsl:text>Pielegniarki posiadające nadgodziny:</xsl:text></b>
</td>
<td>
	<xsl:for-each select="pracownicy/pielegniarki/pielegniarka[@nadgodziny='true']">
		<xsl:value-of select="concat('Imie: ', imie)"/>
		<br/>
		<xsl:value-of select="concat('Nazwisko: ', nazwisko)"/>
		<br/>
	</xsl:for-each>
</td>
```
### 5.div()
```html
<td>
	<b><xsl:text>Średnia wieku wszystkich pacjentów: </xsl:text></b>
</td>
<td>
	<xsl:value-of select="sum(pacjenci/pacjent/wiek) div count(pacjenci/pacjent)"/>
</td>
```
### 6. >
```html
<xsl:if test="substring(@placa,0,5) > 4000">
	<xsl:value-of select="@placa"/>
	<br/>
</xsl:if>
```
### 7. contains()
```html
<xsl:if test="contains(@stan,'dobry')">
	<xsl:value-of select="@producent"/>
	<xsl:text> </xsl:text>
	<xsl:value-of select="model"/>
	<br/>
</xsl:if>
```
## DOM WYMAGANIA - METODY WYKORZYSTUJĄCE DOM
### 1. getElementsByTagName, 2. firstChild
```python
def getValFromElemByTag(element, tag):
    return str(element.getElementsByTagName(tag)[0].firstChild.data)
```
### 3. getAttribute
```python
def getValFromAttrByTag(element, tag):
    return str(element.getAttribute(tag))
```
### 4.  removeAttribute
```python
def poprawnoscPolityczna():
    try:
        for l in lekarze:
            l.removeAttribute("plec")
    except NotFoundErr:
        print("No such attribute in this element!")
```
### 5. hasAttribute, 6. setAttribute
```python
        for s in stacjo:
            if s.hasAttribute("stan"):
                s.setAttribute("stan", "dobry")
```
### 7. cloneNode
```python
nowy = pacjenci.getElementsByTagName("pacjent")[0].cloneNode(deep=True)
```
### 8. createElement
```python
choroba = doc.createElement("choroba")
```
### 9. createTextNode
```python
chorobaText = doc.createTextNode(_choroba)
```
### 10. appendChild
```python
choroba.appendChild(chorobaText)
```
### 11. nodeValue
```python
nowy.getElementsByTagName("imie")[0].firstChild.nodeValue = _imie
```
### 12. removeChild
```python
    for p in pacjenci:
        if p.getElementsByTagName("nazwisko")[0].firstChild.data == _nazwisko:
            szpital.getElementsByTagName("pacjenci")[0].removeChild(p)
```
### 13. node.length, 14. hasChildNodes
```python
def ilePacjentow():
    if pacjenci.hasChildNodes():
        return pacjenci.length
```
### 15.createComment 16. insertBefore
```python
nowy.insertBefore(doc.createComment("NOWY PACJENT"),nowy.getElementsByTagName("imie")[0])
```
