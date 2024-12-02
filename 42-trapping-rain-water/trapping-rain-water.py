class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        # Arrays to store the cumulative max heights on the left and right
        left_max = [0] * n
        right_max = [0] * n

        # Compute left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Compute right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate the trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += max(0, min(left_max[i], right_max[i]) - height[i])

        return trapped_water


