from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize adjacency matrix
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Fill initial prerequisites from the input
        for pr, cr in prerequisites:
            isPrerequisite[pr][cr] = True
        
        # Floyd-Warshall-like transitive closure
        for k in range(numCourses):  # Intermediate node
            for i in range(numCourses):  # Start node
                for j in range(numCourses):  # End node
                    isPrerequisite[i][j] |= isPrerequisite[i][k] and isPrerequisite[k][j]
        
        # Answer queries in O(1) time
        return [isPrerequisite[pr][cr] for pr, cr in queries]
