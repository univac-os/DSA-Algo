class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        DFS so to till last and check terminal and move back
        """
        safe={} #node: T/F
        res=[]
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    #cycle or moving to unsafe node
                    return False
            safe[i]=True
            return safe[i]

        for _ in range(len(graph)):
            if dfs(_):
                res.append(_)
        return res
