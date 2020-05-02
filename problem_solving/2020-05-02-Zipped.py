"""
zip([iterable, ...])

This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

Sample Code

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
Task

The National University conducts an examination of  students in  subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
Input Format

The first line contains  and  separated by a space.
The next  lines contains the space separated marks obtained by students in a particular subject.

Constraints



Output Format

Print the averages of all students on separate lines.

The averages must be correct up to  decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
Sample Output

90.0 
91.0 
82.0 
90.0 
85.5        
Explanation

Marks obtained by student 1: 
Average marks of student 1:

Marks obtained by student 2: 
Average marks of student 2:

Marks obtained by student 3: 
Average marks of student 3:

Marks obtained by student 4: 
Average marks of student 4:

Marks obtained by student 5: 
Average marks of student 5:
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

subject, student = map(int, input().split())
dic = {}
score = []
for i in range(1, student+1):
    score.append(map(float, input().split()))
    # 여기서 우선 테스트 케이스(데이터 타입은 리스트)


for i in zip(*score):
    print(sum(i)/len(i))

"""
zip wants a bunch of arguments to zip together, but what you have is a single argument (a list, whose elements are also lists). The * in a function call "unpacks" a list (or other iterable), making each of its elements a separate argument. So without the *, you're doing zip( [[1,2,3],[4,5,6]] ). With the *, you're doing zip([1,2,3], [4,5,6]).
"""
