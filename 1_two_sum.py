from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in dic:
                dic[target - num] = i
            else:
                return [dic[num], i]
        return []
