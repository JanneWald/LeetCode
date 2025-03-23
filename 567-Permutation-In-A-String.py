def checkInclusion(self, s1: str, s2: str) -> bool:
    # Force s1 to be smaller than s2
    if (len(s1) > len(s2)):
        return False
    
    # Store every characters frequency
    freq = defaultdict(int) 
    for c in s1:
        freq[c] += 1

    l = 0
    for r in range(len(s2)):
        c = s2[r]
        freq[c] -= 1
        # If we have the same char num + length then we checked them all
        if freq[c] == 0 and (r - l + 1) == len(s1):
            return True
        # If we have too many of one character, move left
        while freq[c] < 0:
            freq[s2[l]] += 1
            l += 1
        else:
            pass
    
    return False 
