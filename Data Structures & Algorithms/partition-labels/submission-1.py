class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last = defaultdict(int)
        for i in range(n):
            last[s[i]] = i
        
        ans = []
        max_reach = 0
        start = 0
        for i in range(n):          
            max_reach = max(max_reach, last[s[i]])
           
            if i == max_reach:
                ans.append((i - start + 1))
                start = i + 1

        return ans