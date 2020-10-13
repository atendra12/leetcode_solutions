class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  ## remove extra white spaces
        if(s==""):
            return 0
        words_list = s.split(" ")
        if(words_list[len(words_list)-1]==''):
            return 1
        else:
            return len(words_list[len(words_list)-1])
        