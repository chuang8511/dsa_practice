# Need to solve it again!

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        
        def ableFinishCourse(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not ableFinishCourse(pre): return False
            
            visitSet.remove(crs)
            preMap[crs] = []

            return True

        for i in range(numCourses):
            if not ableFinishCourse(i): return False

        return True

solution = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
solution.canFinish(numCourses, prerequisites)