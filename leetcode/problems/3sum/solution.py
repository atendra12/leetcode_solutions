class Solution:
    def threeSum(self, nums):
        result = set()
        hashmap = dict()
        for index, item in enumerate(nums):
            keys = hashmap.keys()
            if len(keys) == 0:
                hashmap[item] = [index]
                continue
            else:
                for key in keys:
                    third = 0 - item - key
                    if third in keys:
                        poss_triplet = [item, key, third]
                        poss_triplet.sort()
                        if key != third:
                            result.add(tuple(poss_triplet))
                        else:
                            if len(hashmap[key]) >= 2:
                                result.add(tuple(poss_triplet))
            if item in keys:
                hashmap[item].append(index)
            else:
                hashmap[item] = [index]
        
        return result
    
    def check_dup(self, result, triplet):
        """
        Check Duplicates in results
        """
        dup_flag = False
        #val1, val2, val3 = triplet

        for item in result:
            if item == triplet:
                dup_flag = True
                return dup_flag
        return dup_flag

        #for item in result:

        # for item in result:
        #     ## Check item and triplet are duplicate
        #     intr = []
        #     for value in triplet:
        #         if value in item:
        #             intr.append(value)

        #     if len(intr) == 3:
        #         dup_flag = True
        #         return dup_flag
        # return dup_flag

        ## Iterate through nums - first value
            ## find second value from hashkey -- traverse all
            ## find third value as per sum and search in hashkey
                ## If second and third value different -- return triplet
                ## If second and third value is same -- It should have len >=2
                ## return triplet
        ## Add first value into hash
        ## Check if triplet is new to results --- comparing one by one
            ## Order Doesn't matter so check by bag of values - Use union