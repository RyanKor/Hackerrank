"""
The tool {x} will match exactly  repetitions of character/character class/groups.

ach10.png

For Example:

w{3} : It will match the character w exactly  times.
[xyz]{5} : It will match the string of length  consisting of characters {x, y, z}. For example it will match xxxxx, xxxyy and xyxyz.
\d{4} : It will match any digit exactly  times.

Task

You have a test string .
Your task is to write a regex that will match  using the following conditions:

 must be of length equal to 45.
The first  characters should consist of letters(both lowercase and uppercase), or of even digits.
The last  characters should consist of odd digits or whitespace characters.
Note

This is a regex only challenge. You are not required to write any code.
You have to fill the regex pattern in the blank (_________).
"""
import re
Regex_Pattern = r'^[02468a-zA-Z]{40}[13579\s]{5}$'  # Do not delete 'r'.
# 시도한 방법
# 1번 솔루션 (오답)
# r'^\w{40}[13579\s]{5}$' -> \w에 홀수 및 띄어쓰기 포함됨
# 2번 솔루션 (오답)
# r'^[02468\w]{40}[13579\s]{5}$' -> \w가 띄어쓰기 걸러내지 못함

print(str(bool(re.search(Regex_Pattern, input()))).lower())
