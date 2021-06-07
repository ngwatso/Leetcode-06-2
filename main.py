# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        curr = list1
        curr_2 = list2
        temp = list1
        
        while a > 1:
            temp = temp.next
            a -= 1
        
        while b > 0:
            curr = curr.next
            b -= 1
            
        temp.next = curr_2
        
        while curr_2.next is not None:
            curr_2 = curr_2.next
            
        curr_2.next = curr.next
                
        return list1

# ===============

