#Leetcode 707
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.count = 0
        

    def get(self, index: int) -> int:
        node = self.head
        if 0 <= index < self.count:
            for i in range(index+1):
                node = node.next
            return node.val
        else:
            return -1
            
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self.count:
            return
        
        self.count += 1
        newNode = Node(val)
        prev, curr = None, self.head
        for i in range(index + 1):
            prev, curr = curr, curr.next
        else:
            prev.next = newNode
            newNode.next = curr

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.count:
            self.count -= 1
            prev, curr = None, self.head
            for i in range(index + 1):
                prev, curr = curr, curr.next
            else:
                prev.next = curr.next
                curr.next = None
