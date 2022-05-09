#LeetCode 24
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head
        curr = new_head
        while(curr.next != None and curr.next.next != None):
            temp = curr.next
            curr.next = temp.next
            temp2 = temp.next.next
            temp.next.next = temp
            temp.next = temp2
            
            curr = curr.next.next
        return new_head.next
