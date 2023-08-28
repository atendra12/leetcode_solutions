class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def lex_sort(str1, str2):
            length = min(len(str1),len(str2))
            index = 0
            while index < length:
                if str1[index] == str2[index]:
                    index +=1
                    continue
                if order.index(str1[index]) < order.index(str2[index]):
                    return True
                else:
                    return False
            
            if len(str1) > len(str2):
                return False
            
            return True
        
        for i in range(len(words)-1):
            output = lex_sort(words[i],words[i+1])
            if not output:
                return False

        return True
            

