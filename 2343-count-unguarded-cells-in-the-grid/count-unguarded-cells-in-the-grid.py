class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        simulation
        start from each gurad and count the boxes
        """
        obs=set() #both guards and walls as we cant go ahead of them
        for r,c in guards:
            obs.add((r,c))
        for r,c in walls:
            obs.add((r,c))

        visited=set()

        dir=[[0,-1],[0,1],[-1,0],[1,0]]

        for r, c in guards:
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                # Keep going in this direction until hitting obstacle or boundary
                while 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) in obs:
                        break
                    visited.add((nr, nc))
                    nr += dr
                    nc += dc
    
        return m*n - len(obs) - len(visited)