from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = True
            else:
                return True
        return False


# TOPICS: array, hashtable, sorting
# DIFFICULTY: easy
