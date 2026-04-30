# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #brute
        # seen=set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head) 
        #     head=head.next   
        # return False 
         
        #optimal 
        if not head:
            return False
        hare = head.next
        tortoise=head
        while hare and hare.next:
            if hare==tortoise:
                return True
            hare=hare.next.next  
            tortoise = tortoise.next
        return False    

        