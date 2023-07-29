class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## buy at less and sell later at higher
        first = 0
        second = first + 1
        max_profit = 0

        while(second < len(prices)):
            ## check If first is still min value or not
            if prices[first] > prices[second]:
                first = second
                second = first + 1
            else:
                max_profit = max(max_profit, prices[second] - prices[first])
                second += 1

        return max_profit

            

