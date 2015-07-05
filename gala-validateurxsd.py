# Simple XML against XSD Validator for Python 2.7 - 3.2
# to run this script you need additionally: lxml (http://lxml.de)
# author: Gabor Laszlo Hajba, 2013
# source : https://github.com/ghajba/python/tree/master/XSD
# translator : Dominic Boisvert, 2015

import sys
from lxml import etree

xsd_files = []
xml_files = []

def usage():
    print("Utilisation : ")
    print("python XSDValidator.py <liste de fichiers xml> <liste des fichiers xsd>")
    print("Il faut au minumum un fichier .xml et un fichier .xsd.")

def validate_files():
    """ validates every xml file against every schema file"""
    for schema in xsd_files:
        xmlschema = etree.XMLSchema(file=schema)
        for file in xml_files:
            xml_file = etree.parse(file)
            if xmlschema.validate(xml_file):
                print(file + " est valide contre " + schema)
            else:
                log = xmlschema.error_log
                print(file + " est non valide contre " + schema)
                for error in iter(log):
                    print("\tRaison : " + error.message)

def main():
    if(len(sys.argv) < 3):
        usage()
        sys.exit()
    for arg in sys.argv[1:]:
        if arg.lower().endswith(".xml"):
            xml_files.append(arg)
        elif arg.lower().endswith(".xsd"):
            xsd_files.append(arg)
    if len(xsd_files) < 1 or len(xml_files) < 1:
        usage()
        sys.exit()
    validate_files()

if __name__ == '__main__':
    main()
