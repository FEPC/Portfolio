# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:10:53 2019

@author: Fabian Esteban Peña Castillo - 20141020051
"""
#Libraries
import random
import numpy as np

#Variables
#DNA Secuence = la
la = np.full((158),'*')
#Nitrogenous bases = le
le = ['A','C','T','G']
#Segment to add = co
co = np.full((20),'*')
#Concidences in some position = op
op = np.full((139),0)

#Adding nitrogenous bases to the dna sequence
for i in range(0,120):
    num = random.randint(0, 3)
    la[i + 19] = le[num]
    
#Adding nitrogenous bases to the segment   
for i in range(0,20):
    num = random.randint(0, 3)
    co[i] = le[num]

#Compare the segment with the dna sequence
for i in range(0,139):
    for j in range(0,20):
        if la[i+j] == co[j]:
            op[i] +=1

#Looking the position with more coincidences
pos = 0
aux = op[0]
for i in range(0,138):
    if aux < op[i]:
        pos = i
        aux = op[i]
#Auxiliary variables for printing sequences = a1, a2
a1 = np.full((120),'*')
a2 = np.full((pos+1),' ') 

#Filling in auxiliary variables
for i in range(0,120):
    a1[i] = la[i+19]

for i in range(0,20):
    a2[i+(pos-19)] = co[i]

#Print the result
print('Position: ' + str(pos-19))
print('Coinsidences: ' + str(aux))
print("DNA sequences:")
for i in range(0,120):
    print(a1[i] , end=' ')
print()
for i in range(0,pos+1):
    print(a2[i] , end=' ')
    