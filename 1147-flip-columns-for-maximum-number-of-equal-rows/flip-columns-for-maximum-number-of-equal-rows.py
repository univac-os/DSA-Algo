class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashmap = defaultdict(int)
    
        for row in matrix:
            # Convert row to tuple for immutability
            pattern = tuple(row)
            hashmap[pattern] += 1
        
        # Calculate the maximum rows that can be made equal
        max_rows = 0
        for row in hashmap:
            xor_pattern = tuple(1 ^ cell for cell in row)
            max_rows = max(max_rows, hashmap[row] + hashmap.get(xor_pattern, 0))
        
        return max_rows