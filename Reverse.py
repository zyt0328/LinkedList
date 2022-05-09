#Leetcode 206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#双指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,prev, curr =None, None, head
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head

      
#递归算法    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(pre,cur):
            if not cur:
                return pre
                
            tmp = cur.next
            cur.next = pre

            return reverse(cur,tmp)
        
        return reverse(None,head)
