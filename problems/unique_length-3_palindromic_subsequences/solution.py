class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        fullSet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        leftPart = set()
        res = set()
        rightPart = collections.Counter(s)

        for index in range(len(s)):
            rightPart[s[index]] -= 1
            if rightPart[s[index]] == 0:
                rightPart.pop(s[index])
            for char in fullSet:
                if char in leftPart and char in rightPart:
                    res.add((s[index], char))
            leftPart.add(s[index])
        
        return len(res)




        