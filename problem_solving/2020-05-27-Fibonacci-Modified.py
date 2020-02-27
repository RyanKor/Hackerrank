"""
We define a modified Fibonacci sequence using the following definition:

Given terms  and  where , term  is computed using the following relation:

For example, if  and ,

,
,
,
and so on.
Given three integers, , , and , compute and print the  term of a modified Fibonacci sequence.

Function Description

Complete the fibonacciModified function in the editor below. It must return the  number in the sequence.

fibonacciModified has the following parameter(s):

t1: an integer
t2: an integer
n: an integer
Note: The value of  may far exceed the range of a -bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for the size of the result.

Input Format

A single line of three space-separated integers describing the respective values of , , and .

Constraints

 may far exceed the range of a -bit integer.
Output Format

Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are  and .

Sample Input

0 1 5
Sample Output

5
Explanation

The first two terms of the sequence are  and , which gives us a modified Fibonacci sequence of . Because , we return the  term.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.


def fibonacciModified(t1, t2, n):
    i = 2
    # 솔직히 남이 작성한 코드를 가져와 돌렸다.
    # Geeks for Geeks에서 작성된 피보나치 함수를 응용하지 못했다.
    # 난이도를 보고, 쉽다 생각해서 시간을 30분 잡고 풀려 했기 때문이다.
    # 시간이 초과해 결국은 답을 보았다.
    # 동적 프로그래밍인 줄 알았는데, 동적 프로그래밍이 포함 안되도 풀 수 있는 문제였다.
    #print(i, t1 ,t2)
    while(i < n):

        tmp = t1  # t1갑의 변경을 원하지 않기 때문에 변수의 불변성 유지를 목적으로 새로운 객체 생성
        t1 = t2  # 이전의 t2값을 t1에 갱신한다.
        t2 = tmp+t2**2  # 새로운 t2값은 t1 + t2**2 의 형태로 값이 더해진다
        i += 1  # n의 크기 만큼 진행
    return t2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
