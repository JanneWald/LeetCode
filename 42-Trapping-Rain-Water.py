def trap(self, height):
    left = 0
    right = len(height) - 1
    leftMax = height[left] 
    rightMax = height[right]
    res = 0
    while left < right:
        trapped = 0
        # Keep finding the biggest 
        if leftMax <= rightMax:
            left += 1
            leftMax = max(height[left], leftMax)
            trapped = leftMax - height[left] # We already have the min of the 2 maxes, 
        else:
            right -= 1
            rightMax = max(height[right], rightMax)
            trapped = rightMax - height[right]
        if trapped > 0:
            res += trapped
    return res
