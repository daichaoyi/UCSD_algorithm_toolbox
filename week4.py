#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 20:59:16 2022
@author: chaoyidai
"""
# HW1 binary search
def binary_search(vector, scalar):
      left=0
      right=len(vector)
      
      while left<right:
          middle=left+(left+right)//2
          if scalar==vector[middle]:
             return middle
          if scalar>vector[middle]:
             left=middle+1
          if scalar<vector[middle]:
             right=middle-1
      return -1


sequence_one=input("number, sequence one: ").split()   
n1=sequence_one[0]
sequence_one=sequence_one[1:]
sequence_two=input("number, sequence two: ").split()                        
n2=sequence_two[0]
sequence_two=sequence_two[1:]

output=[]
for i in range(len(sequence_two)):
    output.append(binary_search(sequence_one,sequence_two[i]))
print(output)


'''
input format:
5 1 5 8 12 13 
5 8 1 23 1 11

expected format:
2 0 -1 0 -1    
'''




# Problem 2 Majority Element
def majority_element(a):
    if len(a)==0:
        return None
    if len(a)==1:
        return a[0]
    half=len(a)//2
    left=majority_element(a[0:half])
    right=majority_element(a[half:])
    if left==right:
        return left
    if a.count(left)>half:
        return left
    if a.count(right)>half:
        return right
    return None

number=input('number of sequence:')
a=[int(x) for x in input('element of sequence:').split()] 

if majority_element(a)==None:
     print(0)
else:
     print(1)

'''
input:
5 23922
ouput:
1

input:
4 1234
ouput:
0
'''






### Quick Sort(Three-way)`                          
import random
def partition3(a, left, right):
    pivot_value = a[left]
    p_l = i = left
    p_e = right
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes

                                                      

                    
def randomized_quick_sort(a, left, right):
    #如果left>right,说明这个sequence有问题，应该退出
    #如果left=right,说明只有sequence只有一个element,不需要排序，应该退出。
    if left >= right:
        return

    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    pIndex = partition3(a, left, right)
    #pIndex[0] 是divide后的左半翼， pIndex[1]是divide后的右半翼。
    randomized_quick_sort(a, left, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, right)

n = int(input("number of sequence: "))
a = [int(x) for x in input("sequence: ").split()]
randomized_quick_sort(a, 0, n - 1)



               
'''
input:
5 
23922   

output:
22239
'''
















