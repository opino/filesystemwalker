<?xml version="1.0" encoding="UTF-8"?>
<!-- XSLT zum ändern von EdView-konformen XMLs -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0" xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    xmlns="http://www.tei-c.org/ns/1.0">
    <xsl:output method="xml" indent="yes" />      
    <!-- entfernt Leerzeilen, die durch Löschung entstehen -->
    <xsl:strip-space elements="*" />
    <!-- Integrity Template Override -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
<!-- Änderungen für Elemente -->

        <xsl:template match="desc">
            <xsl:element name="description">
                <xsl:attribute name="type">
                    <xsl:value-of>intern</xsl:value-of>
                </xsl:attribute>
                <xsl:value-of select="."/>
            </xsl:element>
        </xsl:template>
    
    <!-- Änderungen für Attribute -->

    <xsl:template match="note/@type[.='intern']">
        <xsl:attribute name="type">
            <xsl:value-of>interna</xsl:value-of>
        </xsl:attribute>
    </xsl:template>
    
</xsl:stylesheet>