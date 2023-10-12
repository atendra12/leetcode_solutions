class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## subproblems
        cost.append(0)
        length = len(cost)
        curr, prev = cost[-2], cost[-1]
        for i in range(3, length+1):
            temp = cost[length - i] + min(curr, prev)
            prev = curr
            curr = temp
        
        return min(curr, prev)


            


        