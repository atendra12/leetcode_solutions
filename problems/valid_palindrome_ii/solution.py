class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -=1

            return True
        
        start = 0
        end = len(s) -1

        while start < end:
            if s[start] == s[end]:
                start +=1
                end -= 1
            else:
                return palindrome(s, start+1, end) or palindrome(s, start, end-1)

        return True 

