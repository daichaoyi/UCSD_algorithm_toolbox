#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:25:26 2022
@author: chaoyidai
"""


# Q1
def fibonacci(n): 
    if n<=1:
        return n 
    return fibonacci(n-1)+fibonacci(n-2)

t=fibonacci(10)
print(t)

# 02
def last_digit(n):
       total=fibonacci(n)
       result=total%10
       return result
   
last_digit(3)    
    
     


# 03
def gcd(a,b):
    if (b==0):
        return a
    else: 
        a,b=b,a%b
        return gcd(a,b)
  
    
    
# 04
        
input= “23” 
a,b=[int(i) for i in input.split()] 
def gcd(a,b):
     if (b==0):
        return b
     else:
        c=b%a
        return gcd(b,c)   
if a>b:
   gcd=gcd(a,b)
else: 
   gcd=gcd(b,a)
print(a*b//gcd)    





# 06
def fibonacci(n): 
    if n<=1:
        return n 
    return fibonacci(n-1)+fibonacci(n-2)
 
def sum_fibonacci(n):
    sum=fibonacci(n)
    while n>0:
        sum+=fibonacci(n-1)
        n=n-1
    return sum%10

t=last_digit_sum_fibonacci(3)
print(t)





# 07
def partial_sum_fibonacci(n,m):
    sum=fibonacci(n)
    while n>m:
        sum+=fibonacci(n-1)
        n=n-1
    return sum%10

t=partial_sum_fibonacci(10,10)
print(t)






# 08
def sum_square_fibonacci(n):
    sum=fibonacci(n)^2
    while n>0:
         sum+=fibonacci(n-1)^2
         n=n-1
    return sum%10

t=sum_square_fibonacci(73)
print(t)




    
    
    
    
    
    
    
    
    
    
    
    