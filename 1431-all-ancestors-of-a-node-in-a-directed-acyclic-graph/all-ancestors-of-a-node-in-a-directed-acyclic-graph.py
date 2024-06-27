class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #reverse edges and dfs to each one O(V+E)
        # we can store the vaue so looks dp 
        # we need that value and its value 
        adjL=defaultdict(list)
        for par,child in edges:
            adjL[child].append(par)

        cache=defaultdict(list)
        def dfs(node):
            if node in cache:
                return cache[node]

            for nei in adjL[node]:
                cache[node]+=[nei]+dfs(nei)

            cache[node]=list(set(cache[node]))
            return cache[node]


        for i in range(n):
            dfs(i)

        return [sorted(cache[_]) for _ in range(n)]