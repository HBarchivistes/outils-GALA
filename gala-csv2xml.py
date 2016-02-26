#!/usr/bin/python
# -*- coding: UTF-8 -*-

# gala-csv2xml.py
# DB - 20160225
# Source et inspiration : http://code.activestate.com/recipes/578384-convert-csv-to-xml/
# Première ligne du fichier csv doit être une entête! Référez-vous au fichier CalendrierConservationExemple.csv.

import csv
import datetime
import uuid
import sys
from lxml import etree

csvFile = 'CalendrierConservation.csv' #Format : une ligne par règle de conservation.
xmlFile = 'CalendrierConservationGala.xml'
csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')

#Ici, on commence à écrire notre fichier xml. SVP conserver les commentaires dans votre fichier xml..
xmlData.write("<?xml version='1.0' encoding='UTF-8'?>" + "\n")
xmlData.write("<!-- Fichier créé avec gala-csv2xml de HB archivistes, s.e.n.c. -->" + "\n")
xmlData.write("<!-- Contacter dominic.boisvert@hbarchivistes.qc.ca pour plus d'informations. -->" + "\n")
xmlData.write("<!-- Fichier généré le " + str(datetime.datetime.now()).split('.')[0] + " -->" + "\n")
xmlData.write("<!-- UUID " + str(uuid.uuid1()) + " -->" + "\n")

# there must be only one top-level tag
xmlData.write('<ROWSET>' + "\n")

rowNum = 0

for row in csvData:
    if rowNum == 0:
        tags = row
    else:
        xmlData.write('<ROW>' + "\n")
        for i in range(0,18):
            xmlData.write('     ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
#Permet d'écrire la section DELAI_ROW pour l'exemplaire principal.
        xmlData.write('       <DELAI>' + "\n")
        xmlData.write('         <DELAI_ROW>' + "\n")
        for princ in range(19,29):
            xmlData.write('         ' + '  <' + tags[princ] + '>' \
                          + row[princ] + '</' + tags[princ] + '>' + "\n")
        xmlData.write('         </DELAI_ROW>' + "\n")
        xmlData.write('       </DELAI>' + "\n")
#Permet d'écrire la section DELAI_ROW pour l'exemplaire secondaire.
        xmlData.write('       <DELAI>' + "\n")
        xmlData.write('         <DELAI_ROW>' + "\n")
        for sec in range(29,39):
            xmlData.write('         ' + '  <' + tags[sec] + '>' \
                          + row[sec] + '</' + tags[sec] + '>' + "\n")
        xmlData.write('         </DELAI_ROW>' + "\n")
        xmlData.write('       </DELAI>' + "\n")
        xmlData.write('</ROW>' + "\n")

    rowNum +=1

xmlData.write('</ROWSET>' + "\n")

#Test pour enlever les nodes vides.
#À développer.

xmlData.close()
