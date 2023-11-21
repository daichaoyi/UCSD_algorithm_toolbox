#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 20:27:37 2022

@author: chaoyidai
"""


#HW1
class solution():

array=[5,7,8,9,10,12]
array_sorted=array.sort(reverse=True)
result=array[0]*array[1]


def max_prod(array):
      element1=max(array)
      array.remove(element1)
      element2=max(array)
      result=element1*element2
      return result












