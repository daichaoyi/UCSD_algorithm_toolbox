#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:34:36 2022

@author: chaoyidai
"""

import math
def money_change(coindeno, total):
     remaincoin=[math.inf]*(total+1)
     remaincoin[0]=0
             
     for i in range(total+1):
          for j in coindeno:
              if i>=j:
                remaincoin[i]=min(remaincoin[i], remaincoin[i-j]+1)
     return remaincoin[total]


total=int(input("the amount that needs to be changed:"))
coindeno=[int(x) for x in input("cointype:").split()]
money_change(coindeno, total)




# HW1  maximum gold
def maximum_gold(totalweight,goldtype):
     remainweight=[math.inf]*300
     remainweight[0]=0    
     
     for i in range(totalweight+1):
        for j in goldtype:
           if i>=j:
               remainweight[i]=min(remainweight[i], remainweight[i-j]+1)
     return remainweight[totalweight]
   
maximum_gold(10,[1,4,8])


    
    
'''
## input
10 3 
1 4 8
## expected output
9
'''







