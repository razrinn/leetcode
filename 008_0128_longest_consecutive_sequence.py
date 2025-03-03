from typing import List

# fix time limit exception by changing starts from list to hashmap
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hmap = {}
        for num in nums:
            hmap[num] = True

        starts = {}

        for num in nums:
            if num - 1 not in hmap:
                starts[num] = True

        tmp = 1
        result = 1
        for num in starts.keys():
            i = num + 1
            while i in hmap:
                tmp += 1
                i += 1
            result = max(tmp, result)
            tmp = 1

        return result

    # second run, more efficient
    def longestConsecutive2(self, nums: List[int]) -> int:
        firsts = set()
        hmap = set(nums)

        for num in hmap:
            if num - 1 not in hmap:
                firsts.add(num)

        res = 0
        for num in firsts:
            tmp = 1
            while num + tmp in hmap:
                tmp += 1
            res = max(res, tmp)

        return res