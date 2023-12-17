class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        stone_dict = Counter(stones)
        count = 0
        for item in jewels:
            try:
                count += stone_dict[item]
            except:
                continue
        return count
        
        """
        count = 0
        for stone in stones:
            if(stone in jewels):
                count += 1
        return count
        """
        