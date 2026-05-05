class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0] * (amount + 1)
        for coin in coins:
            if coin > amount:
                continue

            dp[coin] += 1
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        print(dp)
        return dp[-1]


        