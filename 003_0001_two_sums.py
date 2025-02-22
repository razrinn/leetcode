from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            cur = nums[i]
            if cur in hmap:
                return [i, hmap[cur]]
            hmap[target - cur] = i
