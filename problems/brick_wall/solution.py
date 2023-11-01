class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ## If we can count gaps with position(where they appear) then it would be better
        hashMaps = {0:0}

        for r in wall:
            total = 0
            ## after each entry there is a gap and its index is pre fix sum only. we also don't want end point
            for key in r[:-1]:
                total += key
                hashMaps[total] = 1 + hashMaps.get(total, 0)
        
        return len(wall) - max(hashMaps.values())


        ## Brute force solution but doesn't work when sum is long as we are not interating optmisely
        # prefixSum = [(item[0], 0) for item in wall]
        # maxWidth = sum(wall[0])
        # minCrossLine = len(wall)

        # for line_pos in range(1, maxWidth):
        #     CrossLine = 0
        #     for index in range(len(prefixSum)):
        #         value = prefixSum[index][0]
        #         internal_pt = prefixSum[index][1]
        #         if value < line_pos:
        #             ## Need to increase prefix sum/ value
        #             value += wall[index][internal_pt+1]
        #             ## update value in prefixSum
        #             prefixSum[index] = (value, internal_pt+1)

        #         if value > line_pos:
        #             ## line cross the wall
        #             CrossLine +=1
                
        #     minCrossLine = min(CrossLine, minCrossLine)
        
        # return minCrossLine

                














