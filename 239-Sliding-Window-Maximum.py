def maxSlidingWindow(self, nums, k):
    res = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        # Remove everything less than right val
        while len(q) > 0 and nums[q[-1]] < nums[r]:
            q.pop()
        # Add right val
        q.append(r)

        # Remove left if outside window
        if l > q[0]:
            q.popleft()
        
        # Only move left or add max if we have a k sized window
        if (r - l + 1) == k:
            res.append(nums[q[0]])
            l += 1
        r += 1
    return res
