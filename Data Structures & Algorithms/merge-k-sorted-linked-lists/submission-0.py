import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        qu = []
        count = 1 ## # tiebreaker

        for l in lists:
            heapq.heappush(qu, (l.val, count, l))
            count += 1

        ans = ListNode()
        cur = ans

        while qu:
            _, _, tmp = heapq.heappop(qu)

            cur.next = tmp
            cur = cur.next

            if tmp.next:
                heapq.heappush(qu, (tmp.next.val, count, tmp.next))
                count += 1

        return ans.next

        