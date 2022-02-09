"""
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:

Note that "" represents the consecutive values in between.
Example 

Print the string .
Input Format
The first line contains an integer .

Solution by Mischa van den Burg
www.mischavandenburg.com
"""

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

result = ''

for i in range(n):
    result += str(i+1)
    
print(result)