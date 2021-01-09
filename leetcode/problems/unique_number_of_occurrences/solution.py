class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return (lambda x: len(x) == len(set(x))) (collections.Counter(arr).values())
        """
        from collections import Counter
        count_dict = Counter(arr)
        return len(set(count_dict.values())) == len(count_dict.keys())
        """
        
        