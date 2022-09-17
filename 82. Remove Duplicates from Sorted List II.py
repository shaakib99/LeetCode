# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode(0, head)
        result = r
        fpointer = head and head.next
        
        while fpointer:
            isDuplicate = False
            while fpointer and fpointer.val == result.next.val:
                isDuplicate = True
                fpointer = fpointer.next

            if isDuplicate: result.next = fpointer
            else:
                result = result.next
                result.next = fpointer
                
            fpointer = fpointer and fpointer.next
        return r.next