#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:44:47 2022

@author: chaoyidai
"""

# Problem 1
print('Enter n:')
n=int(input())

def minimum_coin(n):
    accumulator=0
    count=0
    while accumulator<=n-10:
          accumulator+=10
          count+=1

    while accumulator<=n-5:
          accumulator+=5
          count+=1
          
    while accumulator<=n-1:
          accumulator+=1
          count+=1
          
    return count
print(minimum_coin(n))

t=minimum_coin(28)
print(t)

i=list(map(int,input().split()))
n=int(input())








# Problem 2
def maximum_loot(n, capacity, value_list, weight_list):
# calculate the list which contains the unit value for each type of good
    weight_per_unit_list=[]
    for i in range(0,n):
       weight_per_unit=(value_list[i]/weight_list[i])
       weight_per_unit_list.append(weight_per_unit)
                      
# Loop through different types of good     
    weight=0
    value=0
    condition=True
    
    while condition:
                      
          max_index=weight_per_unit_list.index(max(weight_per_unit_list, default=0))
          if weight_list[max_index]<=capacity:
               capacity -= weight_list[max_index]
               value += value_list[max_index]
        
          else:
               fraction=capacity/weight_list[max_index]
               capacity=0
               value += fraction*value_list[max_index]        
          n-=1
          condition=((n != 0) if ((capacity != 0) if True else False) else False)    
          value_list.pop(max_index)
          weight_list.pop(max_index)
          weight_per_unit_list.pop(max_index)
    return value


if __name__=="__main__":
    value_list=[]
    weight_list=[]
    
    n, capacity=map(int,input("n, capacity:").split())

    for i in range(0,n):
        value, weight=map(int,input("value, weight:").split())
        value_list.append(value)
        weight_list.append(weight)
            
print(maximum_loot(n, capacity, value_list, weight_list))


'''
input:
3 50 
60 20 
100 50 
120 30    
solution:
180.0000

input:
1 10 
500 30
solution:
166.66666666666
'''






# Problem 3
def minimum_stop(distance,capacity,num_stop,stop_positions):
   current_miles=0
   output=0 
   for i in range(num_stop):
     if (((stop_positions[i]-current_miles)<=capacity) & ((stop_positions[i+1]-current_miles)>capacity)):
        current_miles=stop_positions[i]
        output+=1
     if (stop_positions[i]-current_miles)>capacity:
         output=-1
         break
   return output
     

if __name__=="__main__":
      distance=int(input("distance:"))
      capacity=int(input("capacity:"))
      num_stop=int(input("number of stop:"))
      stop_positions=list(map(int, input("stop position:").split()))
      stop_positions.append(distance)
      print(minimum_stop(distance,capacity,num_stop,stop_positions))  
          
          
'''
input:        
950
400
4
200 375 550 750     
expected answer:
2

input:
10
3
4 
1 2 5 9
expected answer:
-1
'''





