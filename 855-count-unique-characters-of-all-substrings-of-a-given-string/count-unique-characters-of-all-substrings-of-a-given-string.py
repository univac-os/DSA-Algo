class Solution:
    def uniqueLetterString(self, s: str) -> int:
       
        n = len(s)
        index_map = defaultdict(list)

        # Step 1: collect positions of each character
        for i, ch in enumerate(s):
            index_map[ch].append(i)

        result = 0
        # Step 2: calculate contributions
        for positions in index_map.values():
            positions = [-1] + positions + [n]  # Add sentinels
            for i in range(1, len(positions) - 1):
                prev = positions[i - 1]
                curr = positions[i]
                next = positions[i + 1]
                result += (curr - prev) * (next - curr)

        return result
