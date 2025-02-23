from typing import List

# not optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop from left to right. get the total procuts before i
        # loop from right to left, multiply left_loop[i] to i

        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(1)
                continue
            answer.append(answer[i-1] * nums[i-1])

        p = 1

        for j in reversed(range(len(nums))):
            if j == len(nums) - 1:
                continue
            p = nums[j+1] * p
            answer[j] = answer[j] * p
        return answer