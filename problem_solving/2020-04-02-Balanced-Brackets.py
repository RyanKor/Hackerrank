"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.

isBalanced has the following parameter(s):

s: a string of brackets
Input Format

The first line contains a single integer , the number of strings.
Each of the next  lines contains a single string , a sequence of brackets.

Constraints

, where  is the length of the sequence.
All chracters in the sequences ∈ { {, }, (, ), [, ] }.
Output Format

For each string, return YES or NO.

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES
Explanation

The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line.
The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# 괄호를 이용한 스택, 큐 문제는 백준 등 한국에서 알고리즘 테스트를 제공하는 업체들에서도 자주 사용하는 문제다.
# Complete the isBalanced function below.
# def isBalanced(s):
#     stack = []
#     for parenthese in s:
#         open_ = '{[(' #push로 들어오는 값은 맨 뒤에 쌓이는 형태로 값이 모인다.
#         close_ = '}])' # 이후 pop을 하게 되면, 맨 뒷 값부터 빼내는 형태다.
#         if parenthese in open_: # push 작업을 append로 진행하는 형태
#             stack.append(parenthese)
#         else: #즉, 닫는 parenthese를 처리하는 예외값
#             if open_.find(stack.pop()) != close_.find(parenthese):
#                 return "NO"
#     if not stack:
#         return "YES"
#     else:
#         return "NO"

def matches(a,b):
    if (a=="{" and b=="}") or (a=="(" and b==")") or (a=="[" and b=="]"):
        return True
    else:
        return False
    
def isBalanced(s):
    mystack=[]
    p="NO"
    for i in s:
        if i in ["[","{","("]:
            mystack.append(i)
        else:
            if len(mystack)==0:
                return "NO"
            else:
                b=mystack.pop()
            if matches(b,i):
                p="YES"
            else:
                return "NO"
    if len(mystack)==0:
        return p
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
