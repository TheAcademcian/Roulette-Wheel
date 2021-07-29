"""
Roulette Wheel implementation using Python
"""
import numpy as np
import sys
import random


w = [2,4,4,6] # Weights
v = [4,10,12,3] # Values

weight = 8 # Constraint
col = 4 # Total number of items
row = 4 # Total number of individuals

print("The weights and values are: ")
print("Weights: ", w)
print("Values: ", v)

rand_pop = np.random.randint(0,2,(row,col)) 
rand_popTemp = np.random.randint(0,2,(row,col))

addZeros = np.zeros((row,5))
rand_pop = np.append(rand_pop, addZeros, axis=1)

print(rand_pop[:,0:col])

maxVal = 0
for i in range(row):
    sumWeight = sum(np.multiply(w, rand_pop[i,0:col])) # Total weight calculation
    rand_pop[i,col] = sumWeight
    sumValue = sum(np.multiply(v, rand_pop[i,0:col])) # Total value calculation
    
    if sumWeight>weight: # Constraint checking
        sumValue = 0
        rand_pop[i,col+1] = sumValue
        continue
        
    rand_pop[i,col+1] = sumValue
        
    if maxVal<sumValue:
        maxVal = sumValue
        capIndividual = rand_pop[i,0:col]
        
sumf = sum(rand_pop[:,col+1:col+2])

if sumf == 0:
    print("\nDivide by zero error")
    sys.exit()
    
rand_pop[:,col+2] = np.round(rand_pop[:,col+1]/sumf,2)


rand_pop[0,col+3] =  rand_pop[0,col+2]
for i in range(row-1):
    rand_pop[i+1,col+3] = rand_pop[i,col+3] + rand_pop[i+1,col+2]
    rand_pop[i,col+4] = np.round(random.random(),2)

rand_pop[row-1,col+4] = np.round(random.random(),2)    
        
print("\nThe intermediate calculations: \n",rand_pop[:,0:col+6])

for i in range(row):
    arrayOfTreue = rand_pop[:,col+3]>rand_pop[i,col+4]
    itemindex = np.where(arrayOfTreue == True)[0][0]
    rand_popTemp[i] = rand_pop[itemindex,0:col]

rand_pop[:,0:col] = rand_popTemp

print("\nNext generation: \n",rand_pop[:,0:col])   

