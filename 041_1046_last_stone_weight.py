import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first == second:
                continue

            heapq.heappush(heap, -abs(first-second))

        return -heap[0] if heap else 0