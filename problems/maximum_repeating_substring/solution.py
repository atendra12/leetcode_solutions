class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result = 0
        if(not(word in sequence)):
            return result
        else:
            # if word - size P repeats k times --max p*k= size seq
            for i in range(1,len(sequence)//len(word)+1):
                if(word*i in sequence):
                    result = i
            return result
                
        