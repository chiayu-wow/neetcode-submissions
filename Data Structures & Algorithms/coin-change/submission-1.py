class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## use 1 d dp
        ## if i in coins, dp[i] = 1 if not , we iterate through its prev neighbor to find if current amount can be form
        n = len(coins)
        dp = [math.inf] * (amount + 1)
        coins = set(coins)
        if amount  == 0:
            return 0

        for i in range(1, amount+1):
            if i in coins:
                print("here", i)
                dp[i] = 1
            else:
                for j in range(i-1, 0, -1):
                    if i - j in coins and dp[j] != math.inf:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1] if dp[-1] != math.inf else -1