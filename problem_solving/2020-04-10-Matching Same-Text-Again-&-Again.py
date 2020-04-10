"""
This tool (\1 references the first capturing group) matches the same text as previously matched by the capturing group.

ach18.png

For Example:

(\d)\1: It can match 00, 11, 22, 33, 44, 55, 66, 77, 88 or 99.

Task

You have a test string .
Your task is to write a regex that will match  with the following conditions:

 must be of length: 20
 1character: lowercase letter.
 2character: word character.
 3character: whitespace character.
 4character: non word character.
 5character: digit.
 6character: non digit.
 7character: uppercase letter.
 8character: letter (either lowercase or uppercase).
 9character: vowel (a, e, i , o , u, A, E, I, O or U).
 10character: non whitespace character.
 11character: should be same as 1st character.
 12character: should be same as 2nd character.
 13character: should be same as 3rd character.
 14character: should be same as 4th character.
 15character: should be same as 5th character.
 16character: should be same as 6th character.
 17character: should be same as 7th character.
 18character: should be same as 8th character.
 19character: should be same as 9th character.
 20character: should be same as 10th character.
Note

This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
"""
import re
# Do not delete 'r'.
Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'


print(str(bool(re.search(Regex_Pattern, input()))).lower())
