def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) not in numSet: # If this is the start of a sequence
            current = 1
            while (num + 1) in numSet:
                current += 1
                num += 1
            if current > longest:
                longest = current
    return longest
