from typing import List

# watch solution, need revisit
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i +1, length - 1
            while l < r:
                a, b, c = nums[l], nums[r], nums[i]
                if a + b + c == 0:
                    res.append([a, b, c])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+= 1

                elif a + b + c < 0:
                    l += 1

                else:
                    r -= 1
        return res



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

