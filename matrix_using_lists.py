#taling input of a matrix:
#for equal rows and columns
n = int(input("Enter the number of rows in a matrix"))
a = [[0 for x in range (n)] for y in range(n)]
for i in range (n):
    for j in range(n):
        a[i][j]=int(input())
print(a)

# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# Program to multiply two matrices using nested loops, m X m+1 matix

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


# Program to multiply two matrices (vectorized implementation)

# Program to multiply two matrices (vectorized implementation)
import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# result will be 3x4

result= [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]

result = np.dot(A,B)

for r in result:
	print(r)
