from typing import List


# Just hashmap & array
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        res = []
        for key,val in hmap.items():
            res.append([key, val])

        res = sorted(res, key=lambda x: x[1], reverse=True)
        res = [x[0] for x in res]
        res = res[:k]

        return res