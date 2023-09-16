class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        first, second, index = 0, 0, 0
        while index < m +n:
            if first < m and second < n and temp[first] >= nums2[second]:
                nums1[index] = nums2[second]
                second +=1
            elif first < m and second < n:
                nums1[index] = temp[first]
                first +=1
            elif first == m:
                nums1[index] = nums2[second]
                second +=1
            else:
                nums1[index] = temp[first]
                first+=1
            index +=1









        




        


        