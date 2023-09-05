class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start, end = 0, len(nums) -1
        # while start < end:
        #     if nums[end] == val:
        #         nums[end] = '_'
        #         end -=1
        #         continue
        #     if nums[start] == val:
        #         nums[start] = nums[end]
        #         nums[end] = '_'
        #         start +=1
        #         end -=1
        #     else:
        #         start +=1
        
        # if start == end:
        #     if nums[start] == val:
        #         nums[start] = '_'
        #         return 0

        # return start+1

        # k = 0

        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k+=1

        # return k

        start = 0
        end = len(nums)-1

        while start <= end:
            if nums[end] == val:
                end -=1
                continue
            if nums[start] == val:
                nums[start] = nums[end]
                end -=1
                start +=1
            else:
                start +=1
        
        return start


            
                

            


        
