# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return None

        curr_prev_ptr = None
        curr_ptr = head
        curr_next_ptr = head.next

        while (curr_ptr):
            curr_next_ptr = curr_ptr.next
            curr_ptr.next = curr_prev_ptr
            curr_prev_ptr = curr_ptr
            curr_ptr = curr_next_ptr

        return curr_prev_ptr

