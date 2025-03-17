def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    numsFreq = defaultdict(int)
    freq = [[] for i in range(len(nums) + 1)] #store all possible combination of frequencies
    for num in nums: # Find frequency of all nums
        numsFreq[num] += 1
    # Add the numbers to the list with their frequency as an index
    for n, f in numsFreq.items():
        freq[f].append(n)
    # Go backwards through list and add each num until we have k num
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
