# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
    
        total = 0
        while curr != None:
            total += 1
            curr = curr.next 

        # find the middle one
        total = total//2 + 1

        cur = head
        for i in range(1, total):
            cur = cur.next

        return cur