class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        import functools 
        nums = []
        for index in range(n):
            nums.append(start+2*index)
        return functools.reduce(lambda a,b:a^b,nums)
        