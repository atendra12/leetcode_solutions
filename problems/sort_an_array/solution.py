class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## arr -- nums
        ## sort - asc
        ## merge sort
            ## divide data into sub array -- sort them
                ## rec until only one value is present
            ## given two sorted array merge them -- easy
            ## return merged sorted array
        
    
        def mergeSort(nums, start, end):
            """
            sort arr using merge sort
            """

            ## base cond
                ## single element is sorted only
            if start == end:
                return [nums[start]]

            # Step1: Divide data into sub array
            mid = (start + end) // 2
            ## Step2: Sort each sub array
            left_arr = mergeSort(nums, start, mid)
            right_arr = mergeSort(nums, mid+1, end)
            # Step3: merge them and return sorted arr

            left_arr_len = len(left_arr)
            right_arr_len = len(right_arr)
            left_pt = 0
            right_pt = 0

            merge_arr = []

            while left_pt < left_arr_len and right_pt < right_arr_len :
                if left_arr[left_pt] < right_arr[right_pt]:
                    merge_arr.append(left_arr[left_pt])
                    left_pt +=1
                else:
                    merge_arr.append(right_arr[right_pt])
                    right_pt +=1
            
            while left_pt < left_arr_len:
                merge_arr.append(left_arr[left_pt])
                left_pt +=1
            
            while right_pt < right_arr_len:
                merge_arr.append(right_arr[right_pt])
                right_pt +=1
            
            return merge_arr
        
        return mergeSort(nums, 0, len(nums)-1)



            
        


        