def maxArea(self, heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    most = 0
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        most = max(area, most)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return most
