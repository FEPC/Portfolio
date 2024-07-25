# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:10:53 2019

@author: Fabian Esteban Peña Castillo - 20141020051
"""
import random
import numpy as np

la = np.full((158),'*')
le = ['A','C','T','G']
co = np.full((20),'*')
op = np.full((139),0)


for i in range(0,120):
    num = random.randint(0, 3)
    la[i + 19] = le[num]
    
for i in range(0,20):
    num = random.randint(0, 3)
    co[i] = le[num]

for i in range(0,139):
    for j in range(0,20):
        if la[i+j] == co[j]:
            op[i] +=1

pos = 0
aux = op[0]
for i in range(0,138):
    if aux < op[i]:
        pos = i
        aux = op[i]

a1 = np.full((120),'*')
a2 = np.full((pos+1),' ') 

for i in range(0,120):
    a1[i] = la[i+19]

for i in range(0,20):
    a2[i+(pos-19)] = co[i]
    
print('Posición: ' + str(pos-19))
print('Coinsidencias: ' + str(aux))
for i in range(0,120):
    print(a1[i] , end=' ')
print()
for i in range(0,pos+1):
    print(a2[i] , end=' ')
    