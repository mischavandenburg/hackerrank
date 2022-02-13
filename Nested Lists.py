'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

i struggled for many hours with this one because I was doing it in my local environment and did not account for the float() input
eventually I looked at the discussions and took the logic of a solution I found there, but made my own version.

solution by mischa van den burg
www.mischavandenburg.com
'''

if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name, score])
    
    # put all the scores in a list and sort them
    b = [i[1] for i in a]
    s = sorted(b)

    # remove the lowest number 
    remove_lowest = [i for i in s if i != min(s)]

    # remove all other numbers which are not equal to the second lowest, and create a list of the names which have this value
    second_lowest_only = [i for i in remove_lowest if i == min(remove_lowest)]
    lowest_names = [i[0] for i in a if i[1] == second_lowest_only[0]]

    # print the list of names sorted alphabetically 
    for i in sorted(lowest_names):
        print(i)
    
    

