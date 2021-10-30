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
    #print(arxiu)
    #print(arxiu.name)
    pdf = pdfx.PDFx(str(arxiu))
    pdfjson=pdf.get_metadata()
    if "Title" in pdfjson:
        if not (pdfjson.get('Title') is None):
            #print("Renombrem arxiu de:", arxiu.name, "a:", pdfjson["Title"])
            renombrar(directori, arxiu.name, pdfjson["Title"])
    else:
        print("Arxiu no té títol:", arxiu.name)
    #print(pdfjson)

def renombrar(ruta, antic, nou):
    nomantic = ruta + antic
    nomnou = ruta + nou + ".pdf"
    print("Nom original:", nomantic, "Nom nou:", nomnou)
    os.rename(nomantic, nomnou)

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

directori = "/home/enric/Descargas/telegram/Aportes_informaticos/"
recorreDirectori(directori)
