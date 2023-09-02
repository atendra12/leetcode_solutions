class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # num1_notnum2 = set()
        # num2_notnum1 = set()
        # common_nums = set(nums1).intersection(set(nums2))

        # for item in nums1:
        #     if not item in common_nums:
        #         num1_notnum2.add(item)
        
        # for item in nums2:
        #     if not item in common_nums:
        #         num2_notnum1.add(item)
        
        # return [num1_notnum2, num2_notnum1]

        # nums1 = set(nums1)
        # nums2 = set(nums2)

        # return [[item for item in nums1 if not item in nums2], [item for item in nums2 if not item in nums1]]


        common_nums = set(nums1).intersection(set(nums2))

        return set(nums1) - common_nums, set(nums2) - common_nums



        