from tkinter import *
from Biseccion import *
from Newton import *
from Puntofijo import *
from LU import *

import tkinter as tk

root = tk.Tk()


root.title("Metodos Numericos")
root.geometry('750x350')

def action():
    return x

def actionBisec(vBisec,funcion1,XL,XU,tolerancia):
    resultado = Label(vBisec,text="")
    resultado.place(x=50, y=300)
    Fun = str(funcion1.get())
    xL = float(XL.get())
    xU = float(XU.get())
    tole = float(tolerancia.get())
    val = str(Bisec(Fun,xL,xU,tole))
    res = Fun +" "+ str(xL) +" "+ str(xU) +" "+ str(tole)
    print(res)
    print(val)

    #resultado.configure(text = val)

def actionPfijo(vPfijo,funcion1,xCero,tolerancia):
    resultado = Label(vPfijo,text="")
    resultado.place(x=50, y=300)
    Fun = str(funcion1.get())
    x0 = float(xCero.get())
    tole = float(tolerancia.get())
    val = str(MetodoPF(Fun,x0,tole))
    res = Fun +" "+ str(x0) +" "+" "+ str(tole)
    print(res)
    print(val)
    resultado.configure(text = val)

def actionNewton(vNewton,funcion1,xCero,nIte,tolerancia):
    resultado = Label(vNewton,text="")
    resultado.place(x=50, y=300)
    Fun = str(funcion1.get())
    xinicial = int(xCero.get())
    nIteraciones = int(nIte.get())
    tole = float(tolerancia.get())
    val = str(MetodoPF(Fun,xinicial,tole,nIteraciones))
    #res = Fun +" "+ xinicial +" "+ nIteraciones +" "+ tole
    print(val)
    resultado.configure(text = val)

def actionLU(vlu,funcion1):
    resultado = Label(vlu,text="")
    resultado.place(x=50, y=300)
    Fun = str(funcion1.get())
    val = str(matrizLU(Fun))
    resultado.configure(text = val)

#////////////////////////////////////////////////////////////////////

def Mbiseccion():
    vBisec = tk.Toplevel(root)
    vBisec.title("Biseccion")
    texto = Label(vBisec,text="Biseccion",font=("Orbitron",10))
    texto.place(x=30, y=10)

    f1 = Label(vBisec,text="F: ")
    f1.place(x=20, y=50)
    funcion1 = tk.Entry(vBisec)
    funcion1.place(x=40, y=50)

    xi = Label(vBisec,text="XI: ")
    xi.place(x=20, y=100)
    XL = tk.Entry(vBisec)
    XL.place(x=40, y=100)

    Ni = Label(vBisec,text="XU: ")
    Ni.place(x=20, y=150)
    XU = tk.Entry(vBisec)
    XU.place(x=40, y=150)

    T = Label(vBisec,text="T: ")
    T.place(x=20, y=200)
    tolerancia = tk.Entry(vBisec)
    tolerancia.place(x=40, y=200)

    button2 = tk.Button(vBisec, text="Obtener Valores", command=lambda: actionBisec(vBisec,funcion1,XL,XU,tolerancia))
    button2.place(x=50, y=250, width=100, height=30)

def MPfijo():
    vPfijo = tk.Toplevel(root)
    vPfijo.title("Punto Fijo")
    texto = Label(vPfijo,text="Punto Fijo",font=("Orbitron",10))
    texto.place(x=30, y=10)

    f1 = Label(vPfijo,text="F: ")
    f1.place(x=20, y=50)
    funcion1 = tk.Entry(vPfijo)
    funcion1.place(x=40, y=50)

    xi = Label(vPfijo,text="X0: ")
    xi.place(x=20, y=100)
    xCero = tk.Entry(vPfijo)
    xCero.place(x=40, y=100)

    T = Label(vPfijo,text="T: ")
    T.place(x=20, y=150)
    tolerancia = tk.Entry(vPfijo)
    tolerancia.place(x=40, y=150)

    button = tk.Button(vPfijo, text="Obtener raiz", command=lambda: actionPfijo(vPfijo,funcion1,xCero,tolerancia))
    button.place(x=50, y=250, width=100, height=30)


def Mnewton():
    vNewton = tk.Toplevel(root)
    vNewton.title("Newton")
    texto = Label(vNewton,text="Newton",font=("Orbitron",10))
    texto.place(x=30, y=10)

    f1 = Label(vNewton,text="F: ")
    f1.place(x=20, y=50)
    funcion1 = tk.Entry(vNewton)
    funcion1.place(x=40, y=50)

    xi = Label(vNewton,text="X0: ")
    xi.place(x=20, y=100)
    xCero = tk.Entry(vNewton)
    xCero.place(x=40, y=100)

    Ni = Label(vNewton,text="NI: ")
    Ni.place(x=20, y=150)
    nIte = tk.Entry(vNewton)
    nIte.place(x=40, y=150)

    T = Label(vNewton,text="T: ")
    T.place(x=20, y=200)
    tolerancia = tk.Entry(vNewton)
    tolerancia.place(x=40, y=200)

    button = tk.Button(vNewton, text="Obtener raiz", command=lambda: actionNewton(vNewton,funcion1,xCero,nIte,tolerancia))
    button.place(x=50, y=250, width=100, height=30)

def Mlu():
    vlu = tk.Toplevel(root)
    vlu.title("Factorizacion LU")
    texto = Label(vlu,text="Factorizacion Lu",font=("Orbitron",10))
    texto.place(x=30, y=10)

    nfilas = tk.Entry(vlu)
    nfilas.place(x=40, y=50)

    ncolum = tk.Entry(vlu)
    ncolum.place(x=40, y=100)


    n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))
    #a = n*m
    matriz = []

    for i in range(n):
        matriz.append([])
        for j in range(m):
            val = int(input("ingrese dato"))
            matriz[i].append(val)

    print(matriz)

    f1 = Label(vlu,text="F: ")
    f1.place(x=20, y=50)
    dato = tk.Entry(vlu)
    dato.place(x=40, y=50)

    button = tk.Button(vlu, text="Obtener", command=lambda: (dato,nfilas,ncolum))
    button.place(x=50, y=250, width=100, height=30)








































#Primer Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Soluciones Numericas de ENL",font=("Orbitron",10))
texto.place(x=30, y=10)

Binc = tk.Button(root, text="Busquedas Incrementales",command=action)
Binc.place(x=50, y=50)

Bisec = tk.Button(root, text="Biseccion",command=Mbiseccion)
Bisec.place(x=50, y=100)

Rfalsa = tk.Button(root, text="Regla Falsa",command=action)
Rfalsa.place(x=50, y=150)

Pfijo = tk.Button(root, text="Punto fijo",command=MPfijo)
Pfijo.place(x=50, y=200)

Newton = tk.Button(root, text="Newton",command=Mnewton)
Newton.place(x=50, y=250)

Sec = tk.Button(root, text="Secante",command=action)
Sec.place(x=50, y=300)

Rmul = tk.Button(root, text="Raices Multiples",command=action)
Rmul.place(x=50, y=350)



#Segundo Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Solucion de Sistemas de EL",font=("Orbitron",10))
texto.place(x=300, y=10)

Gauss = tk.Button(root, text="Metodo De Gauss",command=action)
Gauss.place(x=320, y=50)

Lu = tk.Button(root, text="Factorizacion LU",command=Mlu)
Lu.place(x=320, y=100)

Doolitle = tk.Button(root, text="Doolitle",command=action)
Doolitle.place(x=320, y=150)

Crount = tk.Button(root, text="Crount",command=action)
Crount.place(x=320, y=200)

Cholesky = tk.Button(root, text="Cholesky",command=action)
Cholesky.place(x=320, y=250)

Jacobi = tk.Button(root, text="Jacobi",command=action)
Jacobi.place(x=320, y=300)

Gseidel = tk.Button(root, text="Gauss - Seidel",command=action)
Gseidel.place(x=320, y=250)



#Tercer Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Interpolacion",font=("Orbitron",10))
texto.place(x=550, y=10)

Vmonde = tk.Button(root, text="Vandermonde",command=action)
Vmonde.place(x=560, y=50)

Ddiv = tk.Button(root, text="Diferencias Divididas",command=action)
Ddiv.place(x=560, y=100)

Lagrange = tk.Button(root, text="Lagrange",command=action)
Lagrange.place(x=560, y=150)

Splines = tk.Button(root, text="Splines 1 - 2",command=action)
Splines.place(x=560, y=200)


root.mainloop()


