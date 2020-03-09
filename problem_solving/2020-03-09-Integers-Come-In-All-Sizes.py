"""
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

Task
Read four numbers, , , , and , and print the result of .

Input Format
Integers , , , and  are given on four separate lines, respectively.

Constraints




Output Format
Print the result of  on one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232  
Note: This result is bigger than . Hence, it won't fit in the long long int of C++ or a 64-bit integer.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)
