class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for i in range(length):
            if i >0 and nums[i-1]==nums[i]:
                continue
            target = -nums[i]
            j = i+1
            k = length -1
            while(j < k):
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    # result.append([nums[i],nums[j],nums[k]])
                    # j +=1
                    # while nums[j-1] == nums[j] and j<k:
                    #     j+=1
                    
                    while(j<length-1 and nums[j]==nums[j+1]):
                        j+=1
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1

        return result

            
            
        