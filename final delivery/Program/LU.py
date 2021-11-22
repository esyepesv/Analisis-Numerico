import numpy as np

def matrizLU(mat):

    m = len(mat)
    matriz=np.zeros([m,m])
    U=np.zeros([m,m])
    L=np.zeros([m,m])

    matriz=np.array(mat,dtype=float)
    U=np.array(mat,dtype=float)
    #Operaciones para hacer ceros debajo de la diagonal principal

    for k in range(0,m):
        for r in range(0,m):
            if (k==r):
                L[k,r]=1
            if(k<r):
                factor=(matriz[r,k]/matriz[k,k])
                L[r,k]=factor
                for c in range(0,m):
                    matriz[r,c]=matriz[r,c] - (factor*matriz[k,c])
                    U[r,c]=matriz[r,c]
    return L,U

def defmatriz(n,m):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []

    for i in range(n):
        matriz.append([])
        for j in range(m):
            val = int(input("ingrese dato"))
            matriz[i].append(val)

    print(matriz)
#[[4,-2,1],[20,-7,12],[-8,13,17]]
#mat = defmatriz()
'''
(L,U) = matrizLU(mat)
print("Resultados: \n")
print("Matriz L")
print(L)
print("Matriz U")
print(U)'''




