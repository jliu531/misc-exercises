# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:35:24 2018

@author: Jason L
"""
'''
Have the function MatrixPath(strArr) take the strArr parameter being passed 
which will be a 2D matrix of 0 and 1's of some arbitrary size, and determine 
if a path of 1's exists from the top-left #of the matrix to the bottom-right 
of the matrix while moving only in the directions: up, down, left, and right. 
If a path exists your program should return the string true, otherwise your 
program should return the number of #locations in the matrix where if a single
0 is replaced with a 1, a path of 1's will be created successfully. If a path 
does not exist and you cannot create a path by changing a single location in 
the matrix from a 0 to a 1, then #your program should return the string not 
possible. For example: if strArr is ["11100", "10011", "10101", "10011"] 
then this looks like the following matrix: 


1 1 1 0 0
1 0 0 1 1
1 0 1 0 1
1 0 0 1 1 

For the input above, a path of 1's from the top-left to the bottom-right 
does not exist. But, we can change a 0 to a #1 in 2 places in the matrix, 
namely at locations: [0,3] or [1,2]. So for this input your program should 
return 2. The top-left and bottom-right of the input matrix will always be 
1's. 
'''

class UnionFind():
  '''implementation of a union find'''
  def __init__(self, n):
    ids = []
    for i in range(n):
      ids.append(i)
    self.ids = ids
  
  def root(self, a):
    '''finds the root given an id'''
    while a != self.ids[a]:
      a = self.ids[a]
    return a
  
  def unite(self, a, b):
    ''' puts a and b in the same group by chaning the root of b to the root of a'''
    i = self.root(a)
    j = self.root(b)
    self.ids[j] = i
  
  def find(self, a, b):
    return self.root(a) == self.root(b)
    
class strMatrix():
  def __init__(self, strArr):
    self.matrix = [list(row) for row in strArr]
    self.num_rows = len(self.matrix)
    self.num_cols = len(self.matrix[0])
    self.uf_object = UnionFind(self.num_cols*self.num_rows)
  
  def is_path_valid(self):
    '''returns true if there is a path from the top left of the matrix to the
    bottom right, otherwise returns false'''
    return self.uf_object.find(0, len(self.uf_object.ids)-1)
  
  def change_to_one(self, coordinate):
    '''given a coordinate, changes the value of that coordinate to '1' '''
    a, b = coordinate
    self.matrix[a][b] = '1'
  
  def change_to_zero(self, coordinate):
    '''given a coordinate, change the value of that coordinate to '0' '''
    a, b = coordinate
    self.matrix[a][b] = '0'
  
  def get_zeros(self):
    '''returns a list of coordinates that have '0' '''
    coord_list = []
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        if self.matrix[i][j] == '0':
          zero_coord = (i, j)
          coord_list.append(zero_coord)
    return coord_list
  
  def get_neighbors(self, coordinate):
    ''' gets the coordinates of the neighbors of the input coordinate) '''
    neighbors = []
    a, b = coordinate
    if a+1 < self.num_rows:
      neigh = (a+1, b)
      neighbors.append(neigh)
    if a-1 >= 0:
      neigh = (a-1, b)
      neighbors.append(neigh)
    if b+1 < self.num_cols:
      neigh = (a, b+1)
      neighbors.append(neigh)
    if b-1 >= 0:
      neigh = (a, b-1)
      neighbors.append(neigh)
    return neighbors
  
  def get_1d_index(self, coordinate):
    ''' gets the one dimensional index given a coordinate '''
    a, b = coordinate
    return a*self.num_cols + b
  
  def make_connections(self):
    ''' creates connections based on the matrix. 1s are connected to other
    adjacent 1s.'''
    self.uf_object = UnionFind(self.num_cols*self.num_rows)
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        if self.matrix[i][j] == '1':
          neighbors = self.get_neighbors((i, j))
          for neigh in neighbors:
            y, x = neigh
            a = self.get_1d_index((i, j))
            b = self.get_1d_index(neigh)
            if not self.uf_object.find(a, b) and self.matrix[y][x] == '1':
              self.uf_object.unite(a, b)
  
  def to_string(self):
    for row in self.matrix:
      print(f'{row}' + '\n')
              
################################################################################
############################ main ##############################################
################################################################################

strMtx = ["11100", "10011", "10101", "10011"]

mtx = strMatrix(strMtx)
mtx.make_connections()
zeros = mtx.get_zeros()
num_exchanges = 0
exchange_coordintates = []
if mtx.is_path_valid() == True:
  print("Path already exists")
else:
  for zero in zeros:
    mtx.change_to_one(zero)
    mtx.make_connections()
    if mtx.is_path_valid():
      num_exchanges += 1
      exchange_coordintates.append(zero)
    # reset matrix and connections back to original
    mtx.change_to_zero(zero)
    mtx.make_connections()
  
  if num_exchanges == 0:
    print("Not possible")
  else:
    print(f'possible exchanges: {num_exchanges}')
    print(f'at coordinates {exchange_coordintates}')