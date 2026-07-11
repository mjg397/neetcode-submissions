class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max_profit = 0
        #for i in range(len(prices)):
        #    for j in range(i, len(prices)):
        #        profit = prices[j] - prices[i]
        #        if profit > max_profit:
        #            max_profit = profit

        #return max_profit

        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - min(prices[:i+1])
            if profit > max_profit:
                max_profit = profit

        return max_profit
