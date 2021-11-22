from tkinter import *


import tkinter as tk
import sympy as sp
import numpy as np
import pandas as pd

x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)
""" ecuacion tipo: string
    x_0: valor inicial tipo:float
    e_s tolerancia estimada tipo:float"""

def MetodoPF(ecuacion,x_0,es,maxIte):
    global x
    ecuacion=funcion(ecuacion)
    derivada=sp.diff(ecuacion)
    f_NR=x-(ecuacion/derivada)#formula de Newton Rhapson
    ea=100 #error aproximado 100%
    x_r=x_0 #x_i+1
    interaciones=0
    while ea>es:
        x_anterior=x_r# x_anterior = x_i
        x_r=f_NR.evalf(subs={x:x_anterior})
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
        interaciones=interaciones+1
        #print(interaciones,x_r,ea)
        if interaciones>=maxIte:
            #print("\nEl metodo no converge\n")
            break
    return x_r
