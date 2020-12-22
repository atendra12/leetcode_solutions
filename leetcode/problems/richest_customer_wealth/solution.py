class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts))
        """
        for i in range(len(accounts)):
            amount =sum(accounts[i])
            if(amount > wealth):
                wealth = amount
        return wealth
        """