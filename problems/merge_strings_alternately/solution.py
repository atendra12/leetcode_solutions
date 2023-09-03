class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_string = ""
        length = min(len(word1),len(word2))

        for index in range(length):
            merge_string += word1[index] + word2[index]
        
        if index < len(word2)-1:
            merge_string += word2[index+1:]

        if index < len(word1)-1:
            merge_string += word1[index+1:]
        
        return merge_string



    