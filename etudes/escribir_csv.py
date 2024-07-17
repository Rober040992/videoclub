"""
pasos a seguir siempre

abrir el fichero

"""

#escribir un fichero csv
# cada vez que de a run añade lineas "15 y 16"
import csv

fichero = open("data/grupos_zoo.csv", "a", newline= "")

escribidor_csv = csv.writer(fichero, delimiter=";", quotechar= "'")
escribidor_csv.writerow([1,3,1,23]) #para añadir lineas
escribidor_csv.writerow([1,4,1,18]) 

fichero.close() #para guardar

# ahora con dicc

with open("data/grupos_zoo.csv", "a", newline= "") as fichero: #esto abre el fichero directamente (es mas rapido que lo de arriba) no hace falta el close()
    escribidor_csv = csv.DictWriter(fichero, fieldnames= [])