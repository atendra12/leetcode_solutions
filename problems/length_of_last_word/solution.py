class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = 1
        last = len(s) - 1
        count = 0
        while last > -1:
            if s[last] == " " and flag:
                last -=1
                continue
            if s[last] != " ":
                flag = 0
                count +=1
                last -=1
            if s[last] == " ":
                break

        return count





            



