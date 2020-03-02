"""
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123
"""


def printFunction(n):
    result = []
    answer = ''
    for i in range(1, n+1):
        result.append(str(i))
        answer = ''.join(result)
    return int(answer)


if __name__ == '__main__':
    n = int(input())
    answer = printFunction(n)
    print(answer)
