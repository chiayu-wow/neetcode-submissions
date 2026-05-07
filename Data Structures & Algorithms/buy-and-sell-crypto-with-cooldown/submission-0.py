class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        hold, sold, cold = [0]*(n), [0]*(n), [0]*(n)
        hold[0] = -prices[0]

        for i in range(1,n):
            hold[i] = max(
                hold[i-1],
                cold[i-1] - prices[i]
            )

            sold[i] = hold[i-1] + prices[i]

            cold[i] = max(
                cold[i-1],
                sold[i-1]
            )
        
        return max(sold[-1], cold[-1])