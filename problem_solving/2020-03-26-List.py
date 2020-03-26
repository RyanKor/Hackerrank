"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input())
    command = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']
    answer = []
    for i in range(N):
        temp = input().split()
        if temp[0] in command and temp[0] == 'insert':
            answer.insert(int(temp[1]),int(temp[2]))
        elif temp[0] in command and temp[0] == 'print':
            print(answer)
        elif temp[0] in command and temp[0] == 'remove':
            answer.remove(int(temp[1]))
        elif temp[0] in command and temp[0] == 'append':
            answer.append(int(temp[1]))
        elif temp[0] in command and temp[0] == 'sort':
            answer.sort()
        elif temp[0] in command and temp[0] == 'pop':
            answer.pop()
        elif temp[0] in command and temp[0] == 'reverse':
            answer.reverse()