from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length

        cur = 1
        for i in range(length):
            res[i] *= cur
            cur *= nums[i]

        cur = 1
        for i in range(length - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]

        return res


# TOPICS: array, prefixsum
# DIFFICULTY: medium
# NOTES: try to solve array problem with in place changes (without additioanl storage)
