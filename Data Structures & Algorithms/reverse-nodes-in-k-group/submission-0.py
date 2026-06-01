# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        st = []
        dummy = ListNode()
        lastStart = dummy

        cur = head
        while cur:
            st.append(cur)
            cur = cur.next

            if len(st) == k:
                while st:
                    lastStart.next = st.pop()
                    lastStart = lastStart.next

        ## not enough for k
        while st:
            lastStart.next = st.pop(0)
            lastStart = lastStart.next
        
        lastStart.next = None

        return dummy.next
                
        