# Importar la biblioteca
import numpy as np

#crear arreglos de dos dimensiones a partir de listas

miLista=[(1,3,5,7), (2,8,2,4)]

miArreglo= np.array(miLista)
print(miArreglo)

#crear arreglos usando funciones de "relleno"

miArreglo =np.zeros((5,4))

print (miArreglo)

miArreglo= np.ones((5,4))

print (miArreglo)

miArreglo= np.arange (10) #arreglo de datos, hasta 9

print(miArreglo)

miArreglo.reshape((2,10))

miArreglo= np.linspace(0,100,1000)
print(miArreglo)