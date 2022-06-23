# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = "{}".format(head.val)
        while head.next:
            # print(head.next.val)
            s += str(head.next.val)
            head = head.next
        
        return int(s, 2)