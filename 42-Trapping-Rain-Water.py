def trap(self, height: List[int]) -> int:
    def getIncreasing(start, stop, step):
        res = [0] * len(height)
        tallest = 0
        for i in range(start, stop, step):
            if height[i] > tallest:
                tallest = height[i]
            res[i] = tallest
        return res
            
    prefixMax = getIncreasing(0, len(height), 1)
    postfixMax = getIncreasing(len(height) - 1, -1, -1)
    res = 0

    for i in range(len(height)):
        trapped = min(prefixMax[i], postfixMax[i]) - height[i]
        if trapped > 0:
            res += trapped 
    return res
