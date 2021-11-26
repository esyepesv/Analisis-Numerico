from math import sqrt
from sys import exit
import numpy as np

def symmetricMatrix(A):
	"""Calcula la matriz simetrica de A"""

	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if A[i][j] != A[j][i]:
				return False
	return True 

def cholesky(A):
	if not symmetricMatrix(A):
		exit('La matriz no es simetrica')
	n = len(A)
	G = [[0.0]*n for j in range(n)]
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma -= A[k][i]**2
		if suma < 0:
			exit('No es definida positiva')	
		A[i][i] = sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma -= A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0

	return np.array(A)

#mat=[[5,1,3],[1,8,2],[3,2,5]]

def defmatriz(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)

    for i in range(n):
        matriz.append([])
        for j in range(n):
            val = int(input("ingrese dato: "))
            matriz[i].append(val)

    #print(matriz)
    return matriz

mat = defmatriz(input("ingresa el tamaño de la matriz: "))

print("Matriz A")
print(np.array(mat))
resultadoT = cholesky(mat)
resultado=resultadoT.transpose()
print("Matriz L")
print(resultado)
print("Matriz L Transpose")
print(resultadoT)
print("L*LT: ")
print(np.dot(resultado,resultadoT))