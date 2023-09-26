# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def helper(start, end):
            if start > end:
                return 0

            mid = (start + end) // 2

            if guess(mid) == 0:
                return mid

            if guess(mid) < 0:
                return helper(start, mid-1)
            else:
                return helper(mid+1, end)
            
        return helper(1, n)


        