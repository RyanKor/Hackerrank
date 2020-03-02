"""
Task
Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, . The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
"""


def division(a, b):
    print(a//b)
    print(round(a/b, 11))


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    answer = division(a, b)
