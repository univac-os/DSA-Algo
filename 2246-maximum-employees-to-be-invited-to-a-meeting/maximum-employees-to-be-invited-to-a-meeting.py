from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)
        visit = [False] * N
        depth = [-1] * N  # Track depth during traversal
        max_cycle_len = 0  # To track the longest cycle length
        mutual_cycle_len = 0  # To track chains around mutual favorites

        # Step 1: Detect cycles and calculate their lengths
        for i in range(N):
            if visit[i]:
                continue
            
            node = i
            path = []  # To store the current path
            while not visit[node]:
                visit[node] = True
                depth[node] = len(path)
                path.append(node)
                node = favorite[node]

            # Check if a cycle is detected
            if depth[node] != -1:  # Node is part of a cycle
                cycle_start = depth[node]
                cycle_length = len(path) - cycle_start
                max_cycle_len = max(max_cycle_len, cycle_length)

                # Special case for mutual favorites (length 2)
                if cycle_length == 2:
                    mutual_cycle_len += 2

            # Mark all nodes in the path as visited
            for p in path:
                depth[p] = -1

        # Step 2: Handle mutual favorites and calculate chains
        def bfs_longest_chain(src, excluded):
            q = deque([src])
            visited = set([src, excluded])  # Exclude the mutual favorite pair
            length = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for neighbor in reversed_graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                length += 1
            return length - 1  # Subtract 1 to exclude the starting point

        # Build the reversed graph
        reversed_graph = defaultdict(list)
        for i, f in enumerate(favorite):
            reversed_graph[f].append(i)

        # Calculate longest chains for mutual favorites
        for i, f in enumerate(favorite):
            if favorite[f] == i and i < f:  # Mutual favorite pair
                chain1 = bfs_longest_chain(i, f)
                chain2 = bfs_longest_chain(f, i)
                mutual_cycle_len += chain1 + chain2

        return max(max_cycle_len, mutual_cycle_len)
