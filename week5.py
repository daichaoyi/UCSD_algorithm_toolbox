#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:59:58 2022

@author: chaoyidai
"""



# Problem 1
import math
def money_change(coindeno, total):
     remaincoin=[math.inf]*(total+1)
     remaincoin[0]=0
             
     for i in range(total+1):
          for j in coindeno:
              if i>=j:
                remaincoin[i]=min(remaincoin[i], remaincoin[i-j]+1)
     return remaincoin[total]


total=iint(input("the amount that needs to be changed:"))
coindeno=[int(x) for x in input("cointype:").split()]
money_change(coindeno, total)


'''
input
7
[1,3,4,5]

expected answer:
2
'''




# Find the path
import math
number=int(input("number that needs to be decomposed: "))

interm=[math.inf]*(number+1)
interm[0]=0
interm[1]=0

for i in range(2,number+1):
              a=math.inf
              b=math.inf
              c=math.inf
              if (i%2)==0: 
                  a=interm[i//2]+1
              if (i%3)==0:
                  b=interm[i//3]+1
              c=interm[i-1]+1
              interm[i]=min(a,b,c) 

## Find the path of reaching to the large number.
path=[number]
while number>1:
         if ((number%3)==0) & (interm[number]==interm[number//3]+1):
            path.append(number//3) 
            number=number//3
         elif ((number%2)==0) &  (interm[number]==interm[number//2]+1):
            path.append(number//2) 
            number=number//2
         else:
            path.append(number-1)
            number=number-1

path=path[::-1]
length=len(path)-1
print(length)
print(path)




'''
input: 
96234                                                                                                                                                                                                                                                                                                                           
expected answer:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
'''









