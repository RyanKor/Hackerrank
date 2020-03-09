"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be .

Function Description

Complete the libraryFine function in the editor below. It must return an integer representing the fine due.

libraryFine has the following parameter(s):

d1, m1, y1: returned date day, month and year
d2, m2, y2: due date day, month and year
Input Format

The first line contains  space-separated integers, , denoting the respective , , and  on which the book was returned.
The second line contains  space-separated integers, , denoting the respective , , and  on which the book was due to be returned.

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
Explanation

Given the following dates:
Returned: 
Due: 

Because , we know it is less than a year late.
Because , we know it's less than a month late.
Because , we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.


def libraryFine(d1, m1, y1, d2, m2, y2):  # 2가 붙은 일자는 원래 반납 예정일, 1은 실제 반납일
    """
        # 좀더 깔끔한 형태의 답안은 이렇게 작성해야된다.
        if y1>y2:
                return 10000

        if y1==y2:
            if m1>m2:
                return (m1-m2)*500
            if m1==m2 and d1>d2:
                return (d1-d2)*15

        return 0
    """

    # 첫번째 조건, 반납 예정일보다 빨리 반납했을 때
    if y1 < y2:
        return 0
    elif (d1 <= d2 or d1 > d2) and m1 < m2 and y1 <= y2:
        return 0
    elif d1 <= d2 and m1 <= m2 and y1 <= y2:
        return 0
    # elif d1<=d2 and m1<=m2 and y1<=y2:
    #     return 0

    # 두번째 조건, day가 늦은 경우
    if d1 > d2 and m1 <= m2 and y1 <= y2:
        return 15*(d1-d2)
    # 세번째 조건, month가 늦은 경우
    elif m1 > m2 and y1 <= y2:
        return 500*(m1-m2)
    else:
        return 10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
