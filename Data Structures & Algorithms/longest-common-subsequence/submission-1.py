class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## 2 d dp
        ## dp[i][j] = max lCS end at index i in text1 and j in text2
        ## init dp[i][0] = 0 and dp[0][j] = 0
        ## transform = dp[i][j] = max(dp[i-1][j], dp[i][j-1]) , if char same + 
        rows, cols = len(text1), len(text2)
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1  # ✅ 從左上角 +1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])  # ✅ 取上或左最大
                

        return dp[-1][-1]

        