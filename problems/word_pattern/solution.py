class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        hashKey = {}
        hashKey1 = {}
        for index in range(len(pattern)):
            if (pattern[index] in hashKey and hashKey[pattern[index]] != s[index]) or \
                 (s[index] in hashKey1 and hashKey1[s[index]] != pattern[index]):
                return False

            hashKey[pattern[index]] = s[index]
            hashKey1[s[index]] = pattern[index]

        return True

        