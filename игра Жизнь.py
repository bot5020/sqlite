from tkinter import *
import os
import random
import time

def print_mass(mass):
    os.system('cls') 
    for i in mass:
        print(i)
        time.sleep(2)

def count(mass,i,j):
    res = 0
    if mass[i] [j-1] == 1:
        res += 1
    if mass[i-1][j] == 1:
        res += 1
    if mass[i-1][j-1] == 1:
        res += 1
    if mass[i][j+1] == 1:
        res += 1
    if mass[i+1][j] == 1:
        res += 1
    if mass[i+1][j+1] == 1:
        res += 1
    if mass[i+1][j-1] == 1:
        res += 1
    if mass[i-1][j+1] == 1:
        res +=1   
    return res

n = 5
#while True:
mass = []  
for i in range(n):
    mass.append([random.randrange(0, 2) for i in range(n)])
print_mass(mass)
#time.sleep(2)
temp = []
temp = mass.copy()

while True:
    print_mass(mass)
    for i in range (1,len(mass) - 1):
        for j in range (1,len(mass[i]) - 1):
            print (mass[i][j])
            if mass[i][j] == 0 and count(mass,i,j) == 3:
                temp[i][j] = 1
            if (mass[i][j] == 1 and count(mass,i,j) == 2) or count(mass,i,j) == 3 :
                temp[i][j] = 1
            else:
                temp[i][j] = 0
            
            





            
print (count(mass,i,j))

            

#[random.randrange(0, 3,2) for i in range(m)]
#print_mass(mass)    
