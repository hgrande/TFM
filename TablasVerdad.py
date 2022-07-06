import numpy as np #Numpy(Numerical Python) es una librería que nos permite trabajar con arrays. 
#Generador de tablas de verdad
#Preguntamos al usuario el número de variables binarias que tenemos en el problema
# DWaveSampler() lo utilizamos para conectar con el sistema DWave
#EmbeddingComposite lo empleamos para el procedimiento de MinorEmbedding
import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())
numero_variables =int(input("Por favor, introduzca el número de variables binarias que tiene el problema:"))

#El número de filas de la tabla de verdad será 2 elevado al número de variables.
filas = int(2**numero_variables)
#El número de columnas será el número de variables
#La dimensión de la matriz será
#Generamos los valores de cada columna
mitad= int(filas/2)

#Especificamos el tipo de dato que queremos en nuestra matriz:entero
#Creamos matriz ceros. 
arr = np.zeros((filas,numero_variables),dtype='i') 
#Añadimos unos 
for j in range(numero_variables):
    numero_unos = int(2**(numero_variables-j)/2)
    
    for i in range(filas):
   
        if (arr[i-numero_unos,j]==0):

            for l in range(numero_unos):
                arr[i,j]=1
                

print(arr)
