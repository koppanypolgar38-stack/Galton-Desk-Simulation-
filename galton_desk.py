from itertools import count
import math
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.stats import norm

def decision_maker(a,b):
  return random.randint(a,b)

def galton(bulls,levels):
  l=[]
  for i in range(bulls):
    bull_list=[]
    decisions_lists=[]
    for k in range(levels):
      
      if k==0:
        d=decision_maker(0,1)
        decisions_lists.append(d)
      else:
        d=decision_maker(decisions_lists[-1],decisions_lists[-1]+1)
        decisions_lists.append(d)
    bull_list.append(decisions_lists)
    l.append(bull_list)
  
  return l
  
  



#galton(30,10)

bulls=10000
levels=20
l=[galton(bulls,levels)]
#print(l[0][9999][0]) 
galton_last_digit=([l[0][i][0][-1] for i in range(bulls)])
galton_weights=[]
for i in range(levels):
  galton_weights.append(galton_last_digit.count(i))
  
def normalized_exp_value(n):
  l=[]
  for i in range(n):
    k=[]
    if i==0:
      k.append(1)
      
      l.append(k)
      
    else:
      for j in range(1,i+2):
        if j==1 or j==i+1:
          k.append(1/(2**i))
        else:
          k.append((l[-1][j-2]+l[-1][j-1])/2)
      l.append(k)

  
  print(l[-1][len(l[-1])//2]*bulls ) 

def binom(n):
  l=[]
  for i in range(n):
    k=[]
    if i==0:
      k.append(1)
      
      l.append(k)
      
    else:
      for j in range(1,i+2):
        if j==1 or j==i+1:
          k.append(1/(2**i))
        else:
          k.append((l[-1][j-2]+l[-1][j-1])/2)
      l.append(k)
  
  return l[-1]
  
  
  

def variation(n):
  return normalized_exp_value(n)*(1-normalized_exp_value(n))


plt.figure(figsize=(8,3))
plt.bar([i-1 for i in range(len(galton_weights))],galton_weights, alpha=0.6)
plt.plot([i for i in range(len(galton_weights)-1)],[binom(levels-1)[i]*sum(galton_weights) for i in range(len(galton_weights)-1)], color='red', alpha=0.6)
plt.title(f"Levels: {levels}, Lots of balls: {bulls}")
plt.show()

normalized_exp_value(levels-1)

bulls=300
levels=80
l=[galton(bulls,levels)]
#print(l[0][9999][0]) 
galton_last_digit=([l[0][i][0][-1] for i in range(bulls)])
galton_weights=[]
for i in range(levels):
  galton_weights.append(galton_last_digit.count(i))
  
def normalized_exp_value(n):
  l=[]
  for i in range(n):
    k=[]
    if i==0:
      k.append(1)
      
      l.append(k)
      
    else:
      for j in range(1,i+2):
        if j==1 or j==i+1:
          k.append(1/(2**i))
        else:
          k.append((l[-1][j-2]+l[-1][j-1])/2)
      l.append(k)

  
  print(l[-1][len(l[-1])//2]*bulls ) 

def binom(n):
  l=[]
  for i in range(n):
    k=[]
    if i==0:
      k.append(1)
      
      l.append(k)
      
    else:
      for j in range(1,i+2):
        if j==1 or j==i+1:
          k.append(1/(2**i))
        else:
          k.append((l[-1][j-2]+l[-1][j-1])/2)
      l.append(k)
  
  return l[-1]
  
  
  

def variation(n):
  return normalized_exp_value(n)*(1-normalized_exp_value(n))


plt.figure(figsize=(8,3))
plt.bar([i-1 for i in range(len(galton_weights))],galton_weights, alpha=0.6)
plt.plot([i for i in range(len(galton_weights)-1)],[binom(levels-1)[i]*sum(galton_weights) for i in range(len(galton_weights)-1)], color='red', alpha=0.6)
plt.title(f"Balls: {bulls}, lots of levels: {levels} ")
plt.show()

normalized_exp_value(levels-1)

def shifted_decision_maker(a,b,c):
  shift=random.uniform(0,1)
  if shift<=c:
    return a
  else:
    return b



def shifted_galton(balls,levels,shift):
  l=[]
  for i in range(balls):
    bull_list=[]
    decisions_lists=[]
    for k in range(levels):
      
      if k==0:
        d=shifted_decision_maker(0,1,shift)
        decisions_lists.append(d)
      else:
        d=shifted_decision_maker(decisions_lists[-1],decisions_lists[-1]+1,shift)
        decisions_lists.append(d)
    bull_list.append(decisions_lists)
    l.append(bull_list)
  return l

shifted_galton(100,10,0.5)

balls=1000
levels=100
shift=0.25
l=[shifted_galton(balls,levels,shift)]

#print(l[0][9999][0]) 
galton_last_digit=([l[0][i][0][-1] for i in range(balls)])
#print(galton_last_digit)
galton_weights=[]
for i in range(levels):
  galton_weights.append(galton_last_digit.count(i))
  

def binom(n):
  l=[]
  for i in range(n):
    k=[]
    if i==0:
      k.append(1)
      
      l.append(k)
      
    else:
      for j in range(1,i+2):
        if j==1 or j==i+1:
          k.append(1/(2**i))
        else:
          k.append((l[-1][j-2]+l[-1][j-1])/2)
      l.append(k)
  
  return l[-1]
  


plt.figure(figsize=(8,3))
plt.bar([i-1 for i in range(len(galton_weights))],galton_weights, alpha=0.6)
plt.plot([i for i in range(len(galton_weights)-1)],[binom(levels-1)[i]*sum(galton_weights) for i in range(len(galton_weights)-1)], color='red', alpha=0.6)
plt.title(f"Shifted Galton desk by {shift}")
plt.show()

  








