# Importar la biblioteca
import numpy as np

#Una forms de crear arreglos ndarray es usando una lista

miLista=[3,5,7,9]

miArreglo= np.array(miLista)
#dimensiones
print(miArreglo.ndim)  #imprime el numero de ejes, en este caso es 1
print(miArreglo.shape) #imprime una lista con el tamaño de la lista
print(miArreglo.size) #imprime el tamaño
print(miArreglo.dtype) #imprime el tipo 

miArreglo2= np.array([3,6,7,90])   #crear un arreglo a partir de una lista 
