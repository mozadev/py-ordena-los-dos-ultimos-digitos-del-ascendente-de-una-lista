# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 08:27:10 2021

@author: Guillermo Hondermann
"""

import random

def listaUsube(x):
    unidad=x%10
    sobra=x//10
    decena=sobra%10
    if decena<unidad:
        return True
    return False

tamanioLista=int(input("Ingrese el número de elementos de la lista [>10]: "))
while not tamanioLista>10:
    tamanioLista=int(input("Vuelva a ingresar el tamaño de la lista [>10]: "))
lista_original=[]
lista_ultimosDigAscendente=[]
for i in range(tamanioLista):
    númeroAleatorio=random.randint(10, 999)
    lista_original.append(númeroAleatorio)
    if listaUsube(númeroAleatorio):
        lista_ultimosDigAscendente.append(númeroAleatorio)


print("Lista original:", lista_original)

print("lista utimos ascendentes:", lista_ultimosDigAscendente)
