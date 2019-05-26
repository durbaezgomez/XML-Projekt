<!-- <?xml version="1.0" encoding="UTF-8"?> -->
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output indent="yes" method="html" encoding="UTF-8"/>
  <xsl:template match="/szpital">
    <xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html&gt;</xsl:text>
    <html lang="pl">
      
      <head>
        <title>Szpital</title>
        <link rel="stylesheet" type="text/css" href="xsl.css"/>
      </head>
      
      <body>
        <h1>Szpital</h1>
        <xsl:comment>
        To jest opis danych dotyczących szpitala zawartych w pliku xml.
        </xsl:comment>
        <table>
          <tr>
            <td>
              <b><xsl:text>Ilość lekarzy</xsl:text></b> 
            </td>
            <td>
            <xsl:value-of select="count(pracownicy/lekarze/lekarz)"/>
            </td>
          </tr>

          <tr>
            <td>
              <b>
              <xsl:text>Ilość  pielęgniarek: </xsl:text>
              </b> 
            </td>
            <td>
                <xsl:value-of select="count(pracownicy/pielegniarki/pielegniarka)"/>    
            </td>
          </tr>
          <tr>
            <td>
              <b>
              <xsl:text>Ilość pacjentów: </xsl:text>
              </b>
            </td>
            <td>
              <xsl:value-of select="count(pacjenci/pacjent)"/>
            </td>
          </tr>

          <tr>
            <td>
              <b>
                <xsl:text>Średnia wieku wszystkich pacjentów: </xsl:text>
              </b>
            </td>
            <td>
              <xsl:value-of select="sum(pacjenci/pacjent/wiek) div count(pacjenci/pacjent)"/>
            </td>
          </tr>

          <tr>
            <td>
              <b>
                <xsl:text>Wynagrodzenia lekarzy powyżej 4000PLN: </xsl:text>
              </b>
            </td>
            <td>
              <xsl:for-each select="pracownicy/lekarze/lekarz">
                <xsl:if test="substring(@placa,0,5) > 4000">
                  <xsl:value-of select="@placa"/>
                  <br/>
                </xsl:if>
              </xsl:for-each>
            </td>
          </tr>
          <tr>
            <td>
              <b>
                <xsl:text>Lekarze posortowani według zarobków:</xsl:text>
              </b>
            </td>
            <td>
              <xsl:call-template name="zarobki"/>
            </td>
          </tr>

          <tr>
            <td>
              <b>
                <xsl:text>Pielegniarki posiadające nadgodziny:</xsl:text>
              </b>
            </td>
            <td>
              <xsl:for-each select="pracownicy/pielegniarki/pielegniarka[@nadgodziny='true']">
                <xsl:value-of select="concat('Imie: ', imie)"/>
                <br/>
                <xsl:value-of select="concat('Nazwisko: ', nazwisko)"/>
                <br/>
              </xsl:for-each>
            </td>
          </tr>

          <tr>
            <td>
              <b>
                <xsl:text>Komputery w stanie dobrym: </xsl:text>
              </b>
            </td>
            <td>
              <xsl:for-each select="sprzet/rodzaje/komputery/stacjonarne/produkt">
                <xsl:if test="contains(@stan,'dobry')">
                  <xsl:value-of select="@producent"/>
                  <xsl:text> </xsl:text>
                  <xsl:value-of select="model"/>
                  <br/>
                </xsl:if>
              </xsl:for-each>
              <xsl:for-each select="sprzet/rodzaje/komputery/laptopy/produkt">
                <xsl:if test="contains(@stan,'dobry')">
                  <xsl:value-of select="@producent"/>
                  <xsl:text> </xsl:text>
                  <xsl:value-of select="model"/>
                  <br/>
                </xsl:if>
              </xsl:for-each>
            </td>
          </tr>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template name="zarobki">
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
  </xsl:template>

  
</xsl:stylesheet>

