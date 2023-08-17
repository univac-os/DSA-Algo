class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        distance = [[0] * n for _ in range(m)]
        queue = deque()

        # Initialize the queue with all 0s and mark as visited
        for i in range(m):#multi-source array
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i,j))

        # Perform BFS to calculate distances
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                    distance[nx][ny] = distance[x][y] + 1
                    visited.add((nx,ny))
                    queue.append((nx, ny))

        return distance 