from tkinter import *

import threading

#import Biseccion as bi
#from LU import *
import os
import webbrowser

import tkinter as tk

root = tk.Tk()


root.title("Metodos Numericos")
root.geometry('750x400')

ruta = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

'''def action():
    webbrowser.get(ruta).open_new("https://replit.com/@Juan-CamiloC148/Analisis#Busqueda_Incremental.py")

def Biseccion():
    webbrowser.get(ruta).open_new("https://replit.com/@Juan-CamiloC148/Analisis#Biseccion.py"'''
#./S-N-E-N-L/
def binc():
    os.system('start cmd /K python ./S-N-E-N-L/Busqueda_incremental.py')

def bisec():
    os.system('start cmd /K python ./S-N-E-N-L/Biseccion.py')

def rfalsa():
    os.system('start cmd /K python ./S-N-E-N-L/Regla_Falsa.py')

def pfijo():
    os.system('start cmd /K python ./S-N-E-N-L/"Punto fijo.py"')

def newton():
    os.system('start cmd /K python ./S-N-E-N-L/Newton.py')

def sec():
    os.system('start cmd /K python ./S-N-E-N-L/Secante.py')

def rmul():
    os.system('start cmd /K python ./S-N-E-N-L/Raices_Multiples.py')

#./S-S-E-L/

def cholesky():
    os.system('start cmd /K python ./S-S-E-L/Cholesky.py')

def crout():
    os.system('start cmd /K python ./S-S-E-L/Crout.py')

def doolittle():
    os.system('start cmd /K python ./S-S-E-L/Doolittle.py')

def gseidel():
    os.system('start cmd /K python ./S-S-E-L/Gauss-Seidel.py')

def gauss():
    os.system('start cmd /K python ./S-S-E-L/Gauss.py')

def jacobi():
    os.system('start cmd /K python ./S-S-E-L/Jacobi.py')

def lu():
    os.system('start cmd /K python ./S-S-E-L/LU.py')


#./Interpolacion/

def difdiv():
    os.system('start cmd /K python ./Interpolacion/Diferencias_Divididas.py')

def inter():
    os.system('start cmd /K python ./Interpolacion/Interpolacion.py')

def lagrange():
    os.system('start cmd /K python ./Interpolacion/Lagrange.py')

def spline1():
    os.system('start cmd /K python ./Interpolacion/Splines_Grado1.py')

def spline2():
    os.system('start cmd /K python ./Interpolacion/Splines_Grado2.py')

def vander():
    os.system('start cmd /K python ./Interpolacion/Vandermonde.py')



def action(x):
    return x









#Primer Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Soluciones Numericas de ENL",font=("Orbitron",10))
texto.place(x=30, y=10)

Binc = tk.Button(root, text="Busquedas Incrementales",command=binc)
Binc.place(x=50, y=50)

Bisec = tk.Button(root, text="Biseccion",command=bisec)
Bisec.place(x=50, y=100)

Rfalsa = tk.Button(root, text="Regla Falsa",command=rfalsa)
Rfalsa.place(x=50, y=150)

Pfijo = tk.Button(root, text="Punto fijo",command=pfijo)
Pfijo.place(x=50, y=200)

Newton = tk.Button(root, text="Newton",command=newton)
Newton.place(x=50, y=250)

Sec = tk.Button(root, text="Secante",command=sec)
Sec.place(x=50, y=300)

Rmul = tk.Button(root, text="Raices Multiples",command=rmul)
Rmul.place(x=50, y=350)



#Segundo Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Solucion de Sistemas de EL",font=("Orbitron",10))
texto.place(x=300, y=10)

Gauss = tk.Button(root, text="Metodo De Gauss",command=gauss)
Gauss.place(x=320, y=50)

Lu = tk.Button(root, text="Factorizacion LU",command=lu)
Lu.place(x=320, y=100)

Doolitle = tk.Button(root, text="Doolitle",command=doolittle)
Doolitle.place(x=320, y=150)

Crout = tk.Button(root, text="Crount",command=crout)
Crout.place(x=320, y=200)

Cholesky = tk.Button(root, text="Cholesky",command=cholesky)
Cholesky.place(x=320, y=250)

Jacobi = tk.Button(root, text="Jacobi",command=jacobi)
Jacobi.place(x=320, y=300)

Gseidel = tk.Button(root, text="Gauss - Seidel",command=gseidel)
Gseidel.place(x=320, y=350)



#Tercer Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Interpolacion",font=("Orbitron",10))
texto.place(x=550, y=10)

Vmonde = tk.Button(root, text="Vandermonde",command=vander)
Vmonde.place(x=560, y=50)

Ddiv = tk.Button(root, text="Diferencias Divididas",command=difdiv)
Ddiv.place(x=560, y=100)

Lagrange = tk.Button(root, text="Lagrange",command=lagrange)
Lagrange.place(x=560, y=150)

Spline1 = tk.Button(root, text="Splines G1",command=spline1)
Spline1.place(x=560, y=200)

Spline2 = tk.Button(root, text="Splines G2",command=spline2)
Spline2.place(x=560, y=250)

Interpolacion = tk.Button(root, text="Interpolacion",command=inter)
Interpolacion.place(x=560, y=300)



root.mainloop()