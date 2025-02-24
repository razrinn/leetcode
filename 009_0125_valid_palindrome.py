class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <=1:
            return True

        strs = s.lower()
        left = 0
        right = len(strs) - 1

        while left < right:
            if not strs[left].isalnum():
                left += 1
                continue
            if not strs[right].isalnum():
                right -= 1
                continue

            if strs[left] != strs[right]:
                return False

            left += 1
            right -= 1


        return True
