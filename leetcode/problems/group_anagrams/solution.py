class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for item in strs:
            key = [0]*26 ## a...z
            for char in item:
                key[ord(char) - ord('a')] += 1
            anagram_dict[tuple(key)].append(item)

        return anagram_dict.values()
                
