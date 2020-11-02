class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## what about blank string
        if(ransomNote.strip()==''):
            return True
        for letter in set(ransomNote):
            if(magazine.count(letter) < ransomNote.count(letter)):
                return False
        return True
            
            