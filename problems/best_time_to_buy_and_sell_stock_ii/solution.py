class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## return max Profit

        ### low(at lower index), High(at higher index)
            ## multiple times
        
        sum_val = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index-1]:
                sum_val += prices[index] - prices[index-1]
        
        return sum_val

            
        





        









        




        


        

        