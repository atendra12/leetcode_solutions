class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = - heapq.heappop(stones)
            second = - heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, second - first)
            
        heapq.heappush(stones, 0)

        return - heapq.heappop(stones)









        