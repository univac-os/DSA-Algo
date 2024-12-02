class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        stack = []
        trapped_water = 0

        for i in range(n):
            # Process the "valley" when current height is greater than the top of the stack
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break  # No left boundary, can't trap water

                # Calculate the distance between the current index and the stack top (left boundary)
                distance = i - stack[-1] - 1

                # Calculate the bounded height for water trapping
                bounded_height = min(height[i], height[stack[-1]]) - height[top]

                # Add the trapped water for this valley
                trapped_water += distance * bounded_height

            # Push the current index onto the stack
            stack.append(i)

        return trapped_water


# Test case
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
solution = Solution()
print(solution.trap(height))  # Output: 6
