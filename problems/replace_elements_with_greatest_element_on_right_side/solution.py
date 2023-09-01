class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVar = -1
        last = len(arr) - 1
        while last > -1:
            newMax = max(arr[last], maxVar)
            arr[last] = maxVar
            maxVar = newMax
            last -= 1
        return arr
        

            
            





