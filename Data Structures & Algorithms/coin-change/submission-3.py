class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## use 1 d dp
        ## if i in coins, dp[i] = 1 if not , we iterate through its prev neighbor to find if current amount can be form
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != math.inf:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[-1] if dp[-1] != math.inf else -1