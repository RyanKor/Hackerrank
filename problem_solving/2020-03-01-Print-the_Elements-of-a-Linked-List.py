"""
This challenge is part of a MyCodeSchool tutorial track and is accompanied by a video lesson.

If you're new to linked lists, this is a great exercise for learning about them. Given a pointer to the head node of a linked list, print its elements in order, one element per line. If the head pointer is null (indicating the list is empty), don’t print anything.

Input Format

The first line of input contains , the number of elements in the linked list.
The next  lines contain one element each, which are the elements of the linked list.

Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.

Constraints

, where  is the  element of the linked list.
Output Format

Print the integer data for each element of the linked list to stdout/console (e.g.: using printf, cout, etc.). There should be one element per line.

Sample Input

2
16
13
Sample Output

16
13
Explanation

There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the printLinkedList function should print 16 and 13 each in a new line.


"""

#!/bin/python3

import math
import os
import random
import re
import sys

# This is the Single Linked List
# Linked List has Data and Pointer
# The first node called root node.
# the next pointer will be null (None in python)


class SinglyLinkedListNode:  # Node Configuration
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
    # 하나의 노드에는 data, pointer가 같이 붙어 다닌다.
    # Pointer == next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
# 순서도 : SingleLinkedListNode -> SingleLinkedList -> printLinkedList


def printLinkedList(head):
    if head is not None:
        print(head.data)
        printLinkedList(head.next)


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
