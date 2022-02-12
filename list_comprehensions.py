'''
Hackerrank List Comprehensions

You are given three integers  and  representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by i, j, k  on a 3D grid where the sum of is not equal to n. Here, 

This solution took me a while to grasp, but now I get it. 
We get x y z, and i j k represent whatever is between 0 and x y z.

When I grasped that, it was simply a matter of looping over the ranges + 1. 

Solution by Mischa van den Burg

www.mischavandenburg.com

'''

x = 1
y = 1
z = 2
n = 3

solution = [[i, j, k] for i in range(x+1) for j in range(y+1) for  k in range(z+1) if i + j + k != n]

print(sorted(solution))


