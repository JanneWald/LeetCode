def twoSum(self, nums, target):
    numPositions = {}
 
    i = 0
    # Get positions
    for num in nums:
        numPositions[num] = i
        i += 1
    
    # Find pairs
    i = 0
    for num in nums:
        lookingFor = target - num
        if lookingFor in numPositions:
            pos = numPositions[lookingFor]
            if pos != i:
                return [i, pos]
        i += 1
