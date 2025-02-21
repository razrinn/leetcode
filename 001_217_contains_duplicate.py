
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for num in nums:
            if num in hmap:
                return True
            hmap[num] = True

        return False