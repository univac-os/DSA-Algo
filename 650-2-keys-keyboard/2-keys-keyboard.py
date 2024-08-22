class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        
        def dfs(count, paste):
            if count == n:
                return 0
            if count > n:
                return float('inf')  # Use infinity to signify an invalid path
            
            if (count, paste) in cache:
                return cache[(count, paste)]
            
            # Option 1: Paste the current clipboard content
            paste_option = 1 + dfs(count + paste, paste)
            
            # Option 2: Copy all and then paste (2 operations: copy + paste)
            copy_paste_option = 2 + dfs(count + count, count)
            
            cache[(count, paste)] = min(paste_option, copy_paste_option)
            return cache[(count, paste)]
        
        if n == 1:
            return 0
        
        # Start with 1 character on the board and 1 character in the clipboard
        return 1 + dfs(1, 1)
