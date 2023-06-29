class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = prices[0]
        for item in prices:
            if item < min_value:
                min_value = item
            else:
                if profit < item - min_value:
                    profit = item - min_value
        return profit
            


            




            
            



