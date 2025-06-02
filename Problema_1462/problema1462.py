class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        reach = [[False] * numCourses for _ in range(numCourses)]
        
        for u, v in prerequisites:
            reach[u][v] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = True
                        
        result = []
        for u, v in queries:
            result.append(reach[u][v])
        
        return result
