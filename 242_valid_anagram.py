class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_a = {}
        for i in s:
            dic_a[i] = 1 if i not in dic_a else dic_a[i] + 1

        dic_b = {}
        for i in t:
            dic_b[i] = 1 if i not in dic_b else dic_b[i] + 1

        if len(dic_a) != len(dic_b):
            return False

        for k, v in dic_b.items():
            if k not in dic_a or dic_a[k] != v:
                return False
        return True


# TOPIC: hashtable, string, sorting
