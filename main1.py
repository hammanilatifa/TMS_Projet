# Lecture de fichier CSV 
# Remplissage du tableau
import csv
from numpy import random
import pandas as pd

i=0
j=0
rows, cols = (6, 6)
matrix = [[0 for i in range(cols)] for j in range(rows)]

with open("Villes.csv", 'r') as file:
  csvreader = csv.reader(file)
  matrix[0][0]='Villes'
  for row in csvreader:
    i+=1
    matrix[i][0]=row[0]

with open("Villes.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    j+=1
    matrix[0][j]=row[0]

print(matrix)


#seconde code
# Remplissage de la table avec les distance entre les villes

import requests
from ast import literal_eval

i=0
j=0


with open("Villes.csv", 'r') as file :
  csvreader = csv.reader(file)
  for row in csvreader:
    file1 = open('Villes.csv')
    csvreader1 = csv.reader(file1)
    i+=1
    j=0
    for row1 in csvreader1:
      j+=1
      x = requests.get(f'https://api.distancematrix.ai/maps/api/distancematrix/json?origins={row[1]}/{row[2]}&destinations={row1[1]}/{row1[2]}&key=lqvdhBDko1799EBbECtHFiVBhIAvJ')
      data = literal_eval(x.text)
      data= data.get('rows')[0].get('elements')[0].get('distance').get('text')
      if data.split()[1] != 'm':
        matrix[i][j]=float(data.split()[0])
      else:
        matrix[i][j]=0
      

print(matrix)
#data_df = pd.DataFrame(matrix)
#data_df

rows, cols = (5, 5)
economies = [[0 for i in range(cols)] for j in range(rows)]
for i in range(1,6):
  for j in range(1,6):
    economies[i-1][j-1] = matrix[i][1] + matrix[1][j] - matrix[i][j]
 

data_eco = pd.DataFrame(economies)
print(data_eco)


for i in range(1,len(economies)):
  for j in range(1,len(economies)): 
      if((i==j)|(economies[i][j]==economies[j][i])):
        economies[j][i]=0

print('___________')
print(economies)


import numpy as np

T = [1,1]

w, h = 5, 5
mat_null = [[0] * w for i in range(h)]

for i in range(1,len(economies)):
    for j in range(1,len(economies)):   
      if((economies[i][j]==np.max(economies))):
        if ((i+1 not in T) & (j+1 not in T)): 
            T.insert(1,i+1)
            T.insert(2,j+1)
            economies[i][j]=0
            break

while economies != mat_null:
  for i in range(1,len(economies)):
    for j in range(1,len(economies)):   
      if((economies[i][j]==np.max(economies))):
        #print ( i+1 , " ", j+1)
        #print(T)
        if ((i+1 in T) & (j+1 in T)): 
          economies[i][j]=0 
        elif ((i+1 not in T) & (j+1 not in T)): 
          economies[i][j]=0 
        elif((i+1==T[1]) & (j+1 not in T)):
          T.insert(1,j+1)
          economies[i][j]=0 
        elif((i+1==T[len(T)-2]) & (j+1 not in T)):
          T.insert(len(T)-1,j+1) 
          economies[i][j]=0
        elif((j+1==T[1]) & (i+1 not in T)):
          T.insert(1,i+1)
          economies[i][j]=0 
        elif((j+1==T[len(T)-2]) & (i+1 not in T)):
          T.insert(len(T)-1,i+1) 
          economies[i][j]=0 
        else:
          economies[i][j]=0  

print('---------------------Clarke and Wright---------------------') 
print(T)

tounee_Ville = []

for i in range(len(T)):
    tounee_Ville.insert(i,matrix[T[i]][0])

print(tounee_Ville)



#code VNS
print('---------------------VNS---------------------') 

from itertools import permutations
 
nums = [1, 3, 5, 4, 2]


fixed_index= 0 # "Depot"
fixed_element= nums[fixed_index]
newList = []
# create a temporary list with all elements that still are
# missing in the permutation
rest_elements= nums[:fixed_index] + nums[fixed_index+1:]
for permutation in permutations(rest_elements):
    newList.append((fixed_element,) + permutation)

#print(newList)

distances = []
for i in range(len(newList)):
  distance = 0
  for j in range(len(newList[i])-1):
    distance += float(matrix[newList[i][j]][newList[i][j+1]])
  distances.append(distance)


#print(distances)
#print(min(distances))
#print(distances.index(min(distances)))
T_VNS = newList[distances.index(min(distances))]
print(T_VNS)
tounee_Ville_VNS = []

for i in range(len(T_VNS)):
    tounee_Ville_VNS.insert(i,matrix[T_VNS[i]][0])

print(tounee_Ville_VNS)