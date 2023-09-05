"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #looks like graph transversal here we dont need to create adj list as last element are its children
        #so take id--> employee  1-->[1,5,[2,3]]
        empMap={e.id: e for e in employees}
        def dfs(eid):
            employee=empMap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates)
                    )

            
        return dfs(id)
        