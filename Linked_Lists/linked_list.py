#Create head and tail and initialize with null
#Create blank node and assign value to it and reference to null
#Link head and tail with this node
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __iter__(self):
        node = self.head

sll = SLinkedList()
node_1 = Node(1)
node_2 = Node(2)

SLinkedList().head = node_1
SLinkedList().head.next = node_2
SLinkedList().tail = node_2                                                                   