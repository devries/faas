<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fck="http://faas.unnecessary.tech/schema">

  <xsl:template match="/">
    <html>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>Fucks as a Service</title>
      </head>
      <body>
        <xsl:apply-templates/>
        <p>Check out this semantic fucking web page.</p>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="fck:ListOfFucks">
    <h1>Fucks given</h1>
    <xsl:choose>
      <xsl:when test="count(fck:fucks/fck:item) = 0">
        <p>Absolutely no fucks given.</p>
      </xsl:when>
      <xsl:otherwise>
        <ul>
          <xsl:for-each select="fck:fucks/fck:item">
            <li><xsl:value-of select="."/></li>
          </xsl:for-each>
        </ul>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="fck:Error">
    <h1>Error</h1>
    <p style="color: red"><xsl:value-of select="fck:message"/></p>
  </xsl:template>

</xsl:stylesheet>
