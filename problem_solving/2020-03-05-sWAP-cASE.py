"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string .

Constraints


Output Format

Print the modified string .

Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def swap_case(s):
    # pythonic codes - solution 1
    # return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

    # solution 2
    result = []
    for i in s:
        if i.isupper():
            result.append(i.lower())
        else:
            result.append(i.upper())
    return ''.join(result)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
