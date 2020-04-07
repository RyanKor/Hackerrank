"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Constraints

Output Format

Output True or False for each test case on separate lines.

Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
Explanation

Test Case 01 Explanation

Set  = {1 2 3 5 6}
Set  = {9 8 5 6 3 2 1 4 7}
All the elements of set  are elements of set .
Hence, set  is a subset of set .
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
# 아, issubset()이 작동을 안한다. 해당 함수에서 작동을 안하다보니 에러가 나는구나..
for _ in range(int(input())):
    a, A = int(input()), set(map(int, input().split()))
    b, B = int(input()), set(map(int, input().split()))
    if B == B.union(A):
        print(True)
    else:
        print(False)
