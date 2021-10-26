import sys
import os
import json
import pdfx
from pathlib import Path

def recorreDirectori(directori):
    files = Path(directori).glob('**/*.pdf')
    for file in files:
        recuperaMetadata(file)

def recuperaMetadata(arxiu):
    print(arxiu)
    pdf = pdfx.PDFx(str(arxiu))
    pdfjson=pdf.get_metadata()
    #references_list = pdf.get_references()
    references_dict = pdf.get_references_as_dict()
    print(references_dict)
    #if pdfjson[Title]:
    #    print(pdfjson[Title])
    #else:
    #    print("No hi ha titol")
    #    print(pdfjson)
#
#def renombrar(antic, nou):
#    archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
#    nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"
#    os.rename(antic, nou)

# ------------------------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------------------------

#directori("/home/enric/Decargas/telegram/Aportes_informaticos")
#if len(sys.argv) >= 2:
#    pdf = pdfx.PDFx(sys.argv[1])
#    pdfjson=pdf.get_metadata()
#    #print(pdf.get_metadata())
#    print(pdfjson["Title"])
#    #print(pdfjsonp["Title"])
#else:
#    print("Fa falta un paràmetre")/home/enric/Descargas/telegram/Aportes_informaticos

directori = "/home/enric/Descargas/telegram/Aportes_informaticos"
recorreDirectori(directori)
