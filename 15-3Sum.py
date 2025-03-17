def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            return res
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                if (i != left and i != right and left != right):
                    res.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif total > 0:
                right -= 1
            else:
                left += 1
    return res
