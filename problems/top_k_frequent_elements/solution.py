class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for item in nums:
            nums_dict[item] = nums_dict.get(item, 0) + 1
        
        array = [[] for i in range(len(nums)+1)]
        for key, value in nums_dict.items():
            array[value].append(key)

        result = []
        last_pointer = len(array) - 1
        while(k > 0 and last_pointer > -1):
            val = array[last_pointer]
            if val:
                for item in val:
                    result.append(item)
                    k -= 1
            last_pointer -= 1 
            
        return result





        



        

