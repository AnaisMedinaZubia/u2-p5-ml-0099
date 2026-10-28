# Anais Medina NC 0099 fecha 28 de octubre 2026
import numpy as np
import pandas as pd

## datos matriz 4 x 3
Datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas 
# y almacenae la tabla en la variable df dataframe
print(" ----datos apartir de una matriz 4 x 3 ----")
df=pd.DataFrame(Datos_alumno, columns=["ci","marcas", "paquete"])
print(df)

#datos a partir de un diccionario
print(" ---datos apartir de un diccionario ----")
alumno_diccionario = {
    "nombre":["Anais","Alexia","Nahum","Aliah","Jazmin","Diego"],
    "califa":[100,90,100,80,70,50],
    "edad":[16,17,16,16,16,17]
}
estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Anais Medina NC 0099")