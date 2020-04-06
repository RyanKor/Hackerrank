"""
The $ boundary matcher matches an occurrence of a character/character class/group at the end of a line.

matching end items.png


Task

Write a RegEx to match a test string, , under the following conditions:

 should consist of only lowercase and uppercase letters (no numbers or symbols).
 should end in s.
This is a RegEx-only challenge, so you are not required to write any code.
Simply replace the blank (_________) with your RegEx pattern.
"""
import re
Regex_Pattern = r'^[a-zA-Z]*s$'  # Do not delete 'r'.
# 테스트 해본 것 *, + {1,}, {0,}
# +, {1,} -> 주어진 테스트 케이스가 s만 있을 경우, 알파벳이 굳이 존재할 필요가 없다.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
