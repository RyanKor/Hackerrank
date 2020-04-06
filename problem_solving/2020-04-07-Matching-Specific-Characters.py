"""
The character class [ ] matches only one out of several characters placed inside the square brackets.

ach07.png

Task

You have a test string .
Your task is to write a regex that will match  with following conditions:

 must be of length: 6
First character: 1, 2 or 3
Second character: 1, 2 or 0
Third character: x, s or 0
Fourth character: 3, 0 , A or a
Fifth character: x, s or u
Sixth character: . or ,
Note

This is a regex only challenge. You are not required to write any code.
You have to fill the regex pattern in the blank (_________).
"""
import re
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'  # Do not delete 'r'.
# 굉장히 단순한 문제였네..ㅎ

print(str(bool(re.search(Regex_Pattern, input()))).lower())