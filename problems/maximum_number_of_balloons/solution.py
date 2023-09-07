class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = {}
        words = set(list("balloon"))

        for ch in text:
            if ch in words:
                hashMap[ch] = 1 + hashMap.get(ch, 0)
        
        return min(hashMap.get('b',0),hashMap.get('a',0),hashMap.get('l',0)//2, hashMap.get('o',0)//2,hashMap.get('n',0))

