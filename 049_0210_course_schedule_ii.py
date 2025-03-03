from collections import defaultdict
from typing import List

# assisted by chatgpt, need revisit

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for [course, prereq] in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        visited = set()

        res = []

        def dfs(course: int):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res