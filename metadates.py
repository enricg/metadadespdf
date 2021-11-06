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
    try:
        print("{}".format(arxiu.name))
        pdf = pdfx.PDFx(str(arxiu))
        pdfjson=pdf.get_metadata()
        if "Title" in pdfjson:
            if not (pdfjson.get('Title') is None):
                renombrar(directori, arxiu.name, pdfjson["Title"])
        else:
            print("No té títol: {}".format(arxiu.name))
            #print(pdfjson)
            escriure_a_fitxer(json.dumps(pdfjson))
            #escollirNomNou(directori, arxiu.name, pdfjson)
    except ValueError:
            print("No podem llegir les metadades de l'arxiu", arxiu.name)


def escriure_a_fitxer(linia):
    f = open('dadesJSON.txt', 'a')
    try:
        f.write(linia + '\n')
    finally:
        f.close()

def llistaAString(pdfjson):
    linia = ""
    for i in pdfjson:
       linia = linia + i + ","
       return linia

def renombrar(ruta, antic, nou):
    nomantic = ruta + antic
    nomnou = ruta + nou + ".pdf"
    print("Nom original: ", antic, "Nom nou:", nou)
    #print("Nom original: ", nomantic, "Nom nou:", nomnou)
    os.rename(nomantic, nomnou)

def escollirNomNou(ruta, nom, pdfs):
    sortir = False
    while not sortir:
        os.system("clear")
        print("-------------------------------------------------------------")
        print("Nom del pdf: ", nom)
        print("-------------------------------------------------------------")
        posicio = 0
        for clau in pdfs:
            print("| {}  | {} --> {} ".format(posicio, clau, pdfs.get(clau)))
            posicio+=1

        print("-------------------------------------------------------------")
        print("| {} |  Obrir document".format(posicio))
        print("| {} |  Renombrar document de manera manual".format(posicio+1))
        print("| {} |  Saltar al segûent arxiu".format(posicio+2))
        print("-------------------------------------------------------------")
        opcio = int(input("Tria una opció: "))
        if opcio == posicio:
            print("obrir document")
            os.system('st zathura ' + ruta + nom )
        elif opcio == (posicio+1):
            print("renombrar manualment")
            nomNou = input("Escriu el nom per a l'arxiu: ")
            renombrar(ruta, nom, nomNou)
            sortir = True
        elif opcio == (posicio+2):
            print("Saltar al segûent pdf")
            sortir = True
        elif (opcio >= 0 and opcio < posicio):
            print("Has triat una opció possible")
            renombrar(ruta, nom, list(pdfs.values())[opcio])
            sortir = True
        else:
            print("OPCIO INCORRECTE")


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
