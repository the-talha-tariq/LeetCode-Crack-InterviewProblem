class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        buy = prices[0] 
        for day in range(1, len(prices)):  
            if prices[day] < buy:
                buy = prices[day]
            else:
                profit += prices[day] - buy
                buy = prices[day]
        return profit