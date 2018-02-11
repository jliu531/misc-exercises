# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:31:57 2018

@author: Jason L
"""

'''
Have the function FoodDistribution(arr) read the array of numbers stored in arr 
which will represent the hunger level of different people ranging from 0 to 5 
(0 meaning not hungry at all, 5 meaning very hungry). You will also have N 
sandwiches to give out which will range from 1 to 20. The format of the array 
will be [N, h1, h2, h3, ...] where N represents the number of sandwiches you 
have and the rest of the array will represent the hunger levels of different 
people. Your goal is to minimize the hunger difference between each pair of 
people in the array using the sandwiches you have available.

For example: if arr is [5, 3, 1, 2, 1], this means you have 5 sandwiches to 
give out. You can distribute them in the following order to the 
people: 2, 0, 1, 0. Giving these sandwiches to the people their hunger levels 
now become: [1, 1, 1, 1]. The difference between each pair of people is now 0, 
the total is also 0, so your program should return 0. Note: You may not have 
to give out all, or even any, of your sandwiches to produce a minimized 
difference.

Another example: if arr is [4, 5, 2, 3, 1, 0] then you can distribute the 
sandwiches in the following order: [3, 0, 1, 0, 0] which makes all the hunger 
levels the following: [2, 2, 2, 1, 0]. The differences between each pair of 
people is now: 0, 0, 1, 1 and so your program should return the final minimized
difference of 2.
'''
import itertools

def FoodDistribution(arr):
  
  def difference(arr):
    '''returns the sum of the differences between each element of the given list'''
    total = 0
    for i in range(len(arr)-1):
      total += abs(arr[i+1]-arr[i])
    return total
  
  def get_required_sandwiches(arr):
    '''returns the amount of sandwiches needed so that the difference between each pair
    of people is 0'''
    base = min(arr)
    sandwiches = 0
    for i in arr:
      sandwiches += abs(i-base)
    return sandwiches
  
  def get_combinations(n, m):
    '''generate the ways n sandwiches can be distributed to m people'''
    for choice in itertools.combinations(range(n+m-1), n):
        slot = [c-i for i,c in enumerate(choice)]
        result = [0]*m
        for i in slot:
            result[i] += 1
        yield result
  
  def list_subtraction(list1, list2):
    '''performs element wise subtraction with the two lists given, returns false if the resulting
    list contains a negative number'''
    difference = []
    for i in range(len(list1)):
      if list1[i] - list2[i] >= 0:
        difference.append(list1[i] - list2[i])
      else:
        return False
    return difference
  
  #################################### end helpers ############################################################
  
  sandwiches = arr[0]
  people = arr[1:]
  if sandwiches >= get_required_sandwiches(people):
    return 0
  else:
    n_people = len(people)
    diff = None
    for i in range(sandwiches+1):
      sandwich_dist = list(get_combinations(i, n_people))
      for combo in sandwich_dist:
        if list_subtraction(people, combo) != False:
          temp = difference(list_subtraction(people, combo))
          if diff == None or temp < diff:
            diff = temp
  return diff