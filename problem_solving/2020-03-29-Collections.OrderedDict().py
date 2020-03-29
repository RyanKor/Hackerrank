"""
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
Task

You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, .
The next  lines contains the item's name and price, separated by a space.

Constraints


Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
Explanation

BANANA FRIES: Quantity bought: , Price: 
Net Price: 
POTATO CHIPS: Quantity bought: , Price: 
Net Price: 
APPLE JUICE: Quantity bought: , Price: 
Net Price: 
CANDY: Quantity bought: , Price: 
Net Price: 
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
from collections import OrderedDict
ordered_dictionary = OrderedDict()
quantities = []
stuff = []
for i in range(n):
    items = input().split()
    quantities.append(int(items[-1]))
    stuff.append(" ".join(items[:-1]))
    if stuff[i] in ordered_dictionary:
        ordered_dictionary[stuff[i]] += quantities[i]
    else:
        ordered_dictionary[stuff[i]] = quantities[i]


# 코르를 리팩토링하는 과정들 -> answer_stuff라는 새로운 변수를 지정할 필요 없이, stuff라는 변수 지정해서 값을 넣을 때, join으로 한 번에 해결이 가능하다.
# answer_stuff = []
# for i in stuff:
#     i = " ".join(i)
#     answer_stuff.append(i)

# for i in range(len(stuff)):
#     if stuff[i] in ordered_dictionary:
#         ordered_dictionary[stuff[i]] += quantities[i]
#     else:
#         ordered_dictionary[stuff[i]] = quantities[i]

for key, value in ordered_dictionary.items():
    print(key, value)
