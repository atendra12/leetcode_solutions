class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ## BruteForce Solution
        # Hash = collections.Counter(p)
        # N = len(p)
        # res = []
        # for index in range(len(s)):
        #     if collections.Counter(s[index : index+N]) == Hash:
        #         res.append(index)
        
        # return res

        # Better solution
        pcounter = collections.Counter(p)
        N = len(p)
        first = 0
        second = N
        scounter = collections.Counter(s[first:second])
        res = [0] if scounter == pcounter else []
        while second < len(s):
            scounter[s[second]] = scounter.get(s[second], 0) + 1
            scounter[s[first]] -= 1
            if scounter[s[first]] == 0:
                scounter.pop(s[first])
            first += 1
            if scounter == pcounter:
                res.append(first)
            second += 1
        
        return res



        