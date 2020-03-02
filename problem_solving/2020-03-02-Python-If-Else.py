"""
Check Tutorial tab to know how to to solve.

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so we print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it isn't weird. Thus, we print Not Weird.
 """

#!/bin/python3

import math
import os
import random
import re
import sys


def ifElseFunction(n):
    if n % 2 != 0:
        return "Weird"
    if n % 2 == 0 and (n >= 2 and n <= 5):
        return "Not Weird"
    if n % 2 == 0 and (n >= 6 and n <= 20):
        return "Weird"
    if n % 2 == 0 and n > 20:
        return "Not Weird"


if __name__ == '__main__':
    n = int(input().strip())
    answer = ifElseFunction(n)
    print(answer)
