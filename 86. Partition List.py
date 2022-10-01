# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
            Intuition: 
            1. Take all element smaller than x into lNodes
            2. Remove all element smaller than x and create a new Linked List
            3. Join 1 and 2
        '''
        lNodes = ListNode(-1)
        lhead = lNodes
        
        temp = head
        while temp: # Take all element smaller than x int lNodes
            if temp.val < x:
                lNodes.next = ListNode(temp.val)
                lNodes = lNodes.next
            temp = temp.next
        
        temp = ListNode(-1, head)
        thead = temp
        while temp and temp.next: # remove all element smaller than x
            while temp and temp.next and temp.next.val < x:
                temp.next = temp.next.next
            else: temp = temp and temp.next
                
        lNodes.next = thead.next
        
        return lhead.next
        