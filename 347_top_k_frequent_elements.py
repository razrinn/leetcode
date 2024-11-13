import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        maxheap = []
        heapq.heapify(maxheap)

        for num, freq in counts.items():
            heapq.heappush(maxheap, [-freq, num])

        res = []
        for i in range(k):
            _, num = heapq.heappop(maxheap)
            res.append(num)

        return res


# TOPICS: array, hashtable, divideandconquer, sorting, heap, bucketsort, counting, quickselect
# NOTES: solution with heap, must try again with bucketsort
# TODO: NOT SOLVED. TRY THIS QUESTION AGAIN LATER BECAUSE RUNNING OUT OF TIME
