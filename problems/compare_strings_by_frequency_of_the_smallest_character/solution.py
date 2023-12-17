class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # function
        # o(n)
        def f(s):
            return s.count(min(s))
        answer = []
        word_arr = list(map(f,words))
        word_arr.sort()
        from bisect import bisect
        return [len(word_arr)- bisect(word_arr,f(query)) for query in queries]
        ## without bisect
        '''
        
        for item in queries:
            count = 0 
            item_val = f(item)
            for word_val in word_arr:
                if(item_val < word_val):
                    count += 1
                else: break
            answer.append(count)
        return answer
        '''