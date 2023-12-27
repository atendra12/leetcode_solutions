class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # count = 0
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         count += 1
        
        # return False if count > 1 else True

        flag = False
        for i in range(len(nums) -1):
            if flag:
                if nums[i] > nums[i + 1]:
                    return False
            else:
                if nums[i] <= nums[i + 1]:
                    continue
                else:
                    flag = True
                    if i > 0:
                        if min(nums[i], nums[i+1]) >= nums[i - 1]:
                            nums[i] = min(nums[i], nums[i+1])
                        else:
                            nums[i+1] = max(nums[i], nums[i+1])
        return True
                    






