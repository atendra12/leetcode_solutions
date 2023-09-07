class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        IdstoIndex = {n: i for i, n in enumerate(nums1)}
        result = [-1]*len(nums1)

        stack = []
        for item in nums2:
            # if not stack and not item in IdstoIndex:
            #     continue
            while stack and stack[-1] < item:
                val = stack.pop()
                idx = IdstoIndex[val]
                result[idx] = item
            if item in IdstoIndex:
                stack.append(item)
            
        return result









                
                
        