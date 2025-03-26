import heapq
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if k > len(nums):
        return []
    if k == len(nums):
        return [max(nums)]
    if k == 1:
        return nums
    l = 0
    r = k - 1
    res = []
    popNums = defaultdict(int)
    maxHeap = []
    for i in range(0, k):
        maxHeap.append(-nums[i])
    heapq.heapify(maxHeap) # Heapify a max heap

    while(r < len(nums)):
        res.append(-maxHeap[0]) # Get max
        # Remove left
        popNums[nums[l]] += 1
        while (popNums[-maxHeap[0]] > 0):
            popNums[-maxHeap[0]] -= 1
            heapq.heappop(maxHeap)
            
        l += 1
        # Add right 
        r += 1
        if r >= len(nums):
            break
        heapq.heappush(maxHeap, -nums[r])
    
    return res
