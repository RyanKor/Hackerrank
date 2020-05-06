"""
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
# 이 문제를 접근할 때, 배열의 정렬을 응용한 알고리즘 문제로 해석해야하는가,
# 아니면, 다른 종류의 알고리즘 문제인데 정렬의 탈을 뒤집어 쓴 문제로 해석해야 하는가?
# 한 가지 확실한 것은, 정렬의 기본 원리를 잘 활용하는 것은 맞는 사실인 것 같다.
# 1.
# 문제를 보고 느껴지는 확실한 것 한 가지는 대문자가 앞에 있다면, 소문자를 앞에 배치하고 정렬하라는 점
# 2.
# 그리고 숫자가 있다면 홀수를 앞 쪽에 정렬하고, 그 다음 짝수를 정렬하라는 점
# 3.
# 마지막으로 문자가 반드시 앞에 오고 숫자는 뒤에 오되, 숫자는 대문자 뒤에 붙어야한다는 점
# 이런 내용들을 뽑아볼 수 있겠다.

# 4가지 풀이법

# print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
import string
# order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# print(*sorted(input(), key=order.index), sep='')

print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
