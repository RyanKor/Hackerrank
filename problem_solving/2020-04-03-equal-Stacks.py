"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The third line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The fourth line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
Constraints

Output Format

Print a single integer denoting the maximum height at which all stacks will be of equal height.

Sample Input

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1
Sample Output

5
Explanation

Initially, the stacks look like this:

initial stacks

Observe that the three stacks are not all the same height. To make all stacks of equal height, we remove the first cylinder from stacks  and , and then remove the top two cylinders from stack  (shown below).

modified stacks

As a result, the stacks undergo the following change in height:

All three stacks now have . Thus, we print  as our answer.
"""
#!/bin/python3

import os
import sys
from itertools import accumulate
#
# Complete the equalStacks function below.
#
# def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    # 이 경우, 스택이 아예 사용되지 않고, accumulate라는 itertool을 활용해 풀이한 사례다.
    # 파이썬에 대해 더 깊게 이해할 수록, 알고리즘이나 주어진 문제를 풀어가는 과정은 쉬워진다.
    # 다른 사람의 풀이를 쉽게 가져와서 보는 것은, 내가 문제를 풀었을 상황에만 적용하자..
    # 아직은 내가 한참 멀었다는 뜻이다.
#     acc1 = list(accumulate(reversed(h1)))
#     acc2 = list(accumulate(reversed(h2)))
#     acc3 = list(accumulate(reversed(h3)))
#     height = set(acc1) & set(acc2) & set(acc3)
#     height = max(height) if height else 0

#     return height
def makeEqual(s,a):

    ans = sum(s)
    while a < ans:
            top = s[0]
            s.pop(0)
            ans -= top
    return ans

def equalStacks(h1, h2, h3):
    minn = min(sum(h1),sum(h2),sum(h3))
    summ = sum((sum(h1),sum(h2),sum(h3)))
    if minn in range(0,2):
            return minn

    while minn != summ/3:
            ans1 = makeEqual(h1,minn)
            ans2 = makeEqual(h2,minn)
            ans3 = makeEqual(h3,minn)
            minn = min(ans1,ans2,ans3)
            summ = ans1+ans2+ans3
    return summ//3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
