# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        numbers = ""
        
        while current:
            numbers += str(current.val)
            current = current.next
        
        # print(numbers)
        return numbers == numbers[::-1]