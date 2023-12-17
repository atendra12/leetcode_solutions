class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        if length == 1:
            return intervals
        ## let's sort the array
        intervals = sorted(intervals, key=lambda pair: pair[0])

        first_pt = 0
        second_pt = first_pt + 1
        result = []
        while(second_pt < length):
            if intervals[second_pt][0] < intervals[first_pt][0]:
                second_pt, first_pt = first_pt , second_pt
            if intervals[second_pt][0] > intervals[first_pt][1]:
                result.append(intervals[first_pt])
                first_pt = second_pt
                second_pt+=1
            else:
                min_val = min(intervals[first_pt][0], intervals[second_pt][0])
                max_val = max(intervals[first_pt][1], intervals[second_pt][1])
                intervals[first_pt] = [min_val,max_val]
                second_pt+=1

        result.append(intervals[first_pt])
        return result