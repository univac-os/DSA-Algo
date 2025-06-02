class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        restricted_set = set(restricted)
        
        # Build the undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([0])
        visited.add(0)
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for nei in graph[node]:
                if nei not in visited and nei not in restricted_set:
                    visited.add(nei)
                    queue.append(nei)
        
        return count