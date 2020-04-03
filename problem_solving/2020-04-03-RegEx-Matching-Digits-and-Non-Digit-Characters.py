"""
The expression \d matches any digit [ - ].

ach04_01.png



The expression \D matches any character that is not a digit.

ach04_02.png


Task

You have a test string . Your task is to match the pattern 
Here  denotes a digit character, and  denotes a non-digit character.

Note

This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
"""

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 입력되는 test case input에서 regex_pattern을 찾을 것이고,
# 여기서 숫자와 숫자가 아닌 것을 찾아내어 True, False를 분별한다.
# 그리고 문자열화 시켜서 소문자로 만든 값을 출력한다.