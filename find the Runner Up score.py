'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.

solution by mischa van den burg

www.mischavandenburg.com

'''


a = [2, 3, 6, 6, 5]
n = 5

s = sorted(a)
s.reverse()

print(s)

for i in s:
    if i < max(s):
        print(i)
        break

