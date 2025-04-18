from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        # For storing nodes by column
        col_dict = defaultdict(list)
        # BFS queue with (node, col)
        q = deque([(root, 0)])
        min_col, max_col = 0, 0
        
        # Track current level
        level = 0
        
        while q:
            level_size = len(q)
            
            # Process nodes level by level
            for _ in range(level_size):
                node, col = q.popleft()
                
                # Update column range
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                # Store as (level, value) for proper sorting
                col_dict[col].append((level, node.val))
                
                # Add children to queue
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
            
            # Move to next level
            level += 1
        
        # Build result
        result = []
        for col in range(min_col, max_col + 1):
            # Sort values in this column by level, then by value
            col_dict[col].sort()
            result.append([val for _, val in col_dict[col]])
            
        return result