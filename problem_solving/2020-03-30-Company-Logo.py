"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.
"""
#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter

if __name__ == '__main__':
    for each in Counter(sorted(input())).most_common(3): print(*each)
    """
    이게 내가 작성한 답안인데, 반쪽자리 정답이었다. 현재 절반만 맞고, 절반만 틀린 이유를 추측컨데, 알파벳의 갯수가 같을 경우, 알파벳 순으로 정렬해 출력해야하는데, 해당 부분에 대한 답이 빠져 반만 맞은듯하다.
    s = input()
    sorting = {}
    for i in s:
        if i in sorting:
            sorting[i] +=1
        else:
            sorting[i] = 1
    answer = sorted(sorting.items(),key=lambda x: x[1], reverse=True)[:3]
    for key, value in answer:
        print(key, value)
    """