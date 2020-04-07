"""
\b assert position at a word boundary.

Three different positions qualify for word boundaries :
► Before the first character in the string, if the first character is a word character.
► Between two characters in the string, where one is a word character and the other is not a word character.
► After the last character in the string, if the last character is a word character.

ach15.png

Task

You have a test String .
Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U).
The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
The matched word must start and end with a word boundary.

Note

This is a regex only challenge. You are not required to write a code.
You have to fill the regex pattern in the blank (_________).
"""
import re
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
# 문제의 설명처럼 'The matched word must start and end with a word boundary.'를 만족시키기 위해
# 맨 앞에 ^, 맨 뒤에 $를 붙여 패턴 값을 지정했는데 그 문제는 왜 답이 되지 않을까?


print(str(bool(re.search(Regex_Pattern, input()))).lower())
