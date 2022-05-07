#LeetCode 203
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None:
            if head.val == val:
                return None
            else:
                return head
        prev = head
        curr = head.next
        while curr != None:
            print(prev.val)
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next
            
        if head.val == val:
            head = head.next
        return head
