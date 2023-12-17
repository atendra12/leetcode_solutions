class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_canday_value = max(candies)
        output = []
        for index in range(len(candies)):
            if(candies[index]+extraCandies >= max_canday_value):
                output.append(True)
            else:
                output.append(False)
        return output