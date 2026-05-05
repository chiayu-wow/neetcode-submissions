class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []
        for i in range(len(height)):
            cur = height[i]

            while st and cur >= height[st[-1]]:
                    j = st.pop()
                    
                    if not st:
                        break

                    ans += (min(cur, height[st[-1]]) - height[j]) * (i - st[-1] - 1)
            st.append(i)
        return ans