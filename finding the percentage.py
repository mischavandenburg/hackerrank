'''
"The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal."

Solution by Mischa van den Burg
www.mischavandenburg.com
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()    
    
    numbers = student_marks[query_name]
    total = 0
    
    for i in numbers:
        total += i

    divided = total / int(len(numbers))
    formatted_float = format(divided, ".2f")
        
    print(format(divided, ".2f"))
    