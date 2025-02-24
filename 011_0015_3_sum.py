from typing import List

# Brute force, time limit exception
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        a = 0
        b = 1
        c = 2

        res = []
        hmap = {}

        while a <= length - 3:
            i = nums[a]
            j = nums[b]
            k = nums[c]

            c+= 1
            if i + j == -k:
                key = "".join(str(c) for c in sorted([i,j,k]))
                if key not in hmap:
                    res.append([i, j, k])
                    hmap[key] = True

            if c == length:
                b += 1
                c = b + 1

            if b == length - 1:
                a += 1
                b = a + 1
                c = b + 1

        return res