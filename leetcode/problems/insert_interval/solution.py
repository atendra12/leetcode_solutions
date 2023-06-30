class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        length = len(intervals)
        first = True
        if length ==0:
            result.append(newInterval)
        for index, item in enumerate(intervals):
            if item[1] < newInterval[0]:
                result.append(item)
                if index >= length-1:
                    result.append(newInterval)
            elif newInterval[1] < item[0]:
                if first:
                    result.append(newInterval)
                    first = False
                result.append(item)
            else:
                newInterval[0] = min(item[0], newInterval[0])
                newInterval[1] = max(item[1], newInterval[1])
                first = True
                if index >= length-1:
                    result.append(newInterval)

        return result
        





            


