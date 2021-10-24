import sys
import os
import json
import pdfx


#def renombrar(antic, nou):
#    archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
#    nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"
#    os.rename(antic, nou)

# ------------------------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------------------------

if len(sys.argv) >= 2:
    pdf = pdfx.PDFx(sys.argv[1])
    pdfjson=pdf.get_metadata()
    #print(pdf.get_metadata())
    print(pdfjson["Title"])
    #print(pdfjsonp["Title"])
else:
    print("Fa falta un paràmetre");
