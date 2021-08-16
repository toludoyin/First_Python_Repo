#NUMPY
import numpy as np
>>> a = np.arange(36).reshape(6,6)
>>> a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])

>>> a.ndim
2
>>> a.size
36
>>> a.itemsize
8

>>> #indexing and slicing
>>> a[0,4]
4
>>> a[0:3]
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]])

>>> a[-1]
array([30, 31, 32, 33, 34, 35])

>>> a[0:5,3]
array([ 3,  9, 15, 21, 27])

>>> a[-1,2:4]
array([32, 33])

>>> a[:,2:6]
array([[ 2,  3,  4,  5],
       [ 8,  9, 10, 11],
       [14, 15, 16, 17],
       [20, 21, 22, 23],
       [26, 27, 28, 29],
       [32, 33, 34, 35]])

>>> #iterate through an array
>>> import numpy as np
>>> a = np.array([[2,3,5],[4,8,90],[1,5,7]])
>>> a
array([[ 2,  3,  5],
       [ 4,  8, 90],
       [ 1,  5,  7]])
>>> for row in a:
	print(row)

[2 3 5]
[ 4  8 90]
[1 5 7]
>>>
>>> for column in row:
	print(column)

1
5
7
>>> for cell in a.flat:
	print(cell)

2
3
5
4
8
90
1
5
7

>>> #stacking 2array together
import numpy as np
>>> a = np.arange(12).reshape(3,4)
>>> b = np.arange(24,36).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

>>> b
array([[24, 25, 26, 27],
       [28, 29, 30, 31],
       [32, 33, 34, 35]])

>>> np.vstack((a,b))
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [24, 25, 26, 27],
       [28, 29, 30, 31],
       [32, 33, 34, 35]])

>>> np.hstack((a,b))
array([[ 0,  1,  2,  3, 24, 25, 26, 27],
       [ 4,  5,  6,  7, 28, 29, 30, 31],
       [ 8,  9, 10, 11, 32, 33, 34, 35]])

>>>#spliting
z = np.arange(30).reshape(2,15)
>>> z
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

>>> np.hsplit(z,3)
[array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])]

>>> result =np.hsplit(z,3)
>>> result[0]
array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]])
>>> result[1]
array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]])
>>> result[2]
array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])

>>> result = np.vsplit(z,3)
result = np.vsplit(z,2)
>>> result[0]
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])
>>> result[1]
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

>>> #indexing with boolean
r = np.arange(30).reshape(3,10)
>>> r
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

>>> y = r > 20
>>> y
array([[False, False, False, False, False, False, False, False, False,
        False],
       [False, False, False, False, False, False, False, False, False,
        False],
       [False,  True,  True,  True,  True,  True,  True,  True,  True,
         True]])
>>> r[y]
array([21, 22, 23, 24, 25, 26, 27, 28, 29])
>>> r[y] = 0

>>> r
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20,  0,  0,  0,  0,  0,  0,  0,  0,  0]])


