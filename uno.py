# Importamos las funciones y paquetes que vamos a usar
from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel
#Esta parte es la traducción
import numpy as np
#Variables no binarias. Restrición tipo x + y = a con a>2. F.o. tipo xy
#Creamos la matriz de la función objetivo

ti = int(input("Introduce el término independiente:"))
variables = ti **2
print("El número de variables es",variables)
a = np.zeros(shape=(ti, ti))

for i in range(ti):
    for j in range(ti):

        if j>=i:
            a[i,j]= (i+1)*(j+1)

print(a)
# a sería la matriz asociada a la función objetivo
# Creamos ahora b ,la matriz asociada a la restricción
# Recordemos que sumamos el valor (a - (x+y))^2 a la función objetivo. Hallemos la matriz asociada a esa expresión
# Recordemos también que la constante a**2 que sale al operar, no influye para nada en nuestro proceso de optimización
# Por lo tanto, no la añadiremos en nuestra expresión matricial.
b = np.zeros(shape=(ti, ti))
for i in range(ti):
    for j in range(ti):
        if i==j:
            b[i,j]= 1
        if j > i:
            b[i,j]= 2
        
print(b)
# Sumamos las dos para obtener los coeficientes de nuestra función objetivo total:
c = np.zeros(shape=(ti, ti))
for i in range(ti):
    for j in range(ti):
        c[i,j]= a[i,j]+b[i,j]
print(c)


# Define the problem as a Python dictionary and convert it to a BQM
for i in range(ti):
    for j in range(ti):
        Q = {(i,j):c[i,j]}
       

# Convert the problem to a BQM
bqm = BinayQuadraticModel.from_qubo(Q)

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample(bqm,num_reads = 10)
print(sampleset)

# EL modelo QUBO es una función objetivo de variables binarias representadas como una matriz diagonal superior,
# donde los términos de la digonal son los coeficientes lineales y los términos no nulos de fuera de la diagonal son los coeficientes cuadráticos.

#    E(x) = sumatorio xi * Qi,j * xj               xi € {0,1}
#             i<=j 