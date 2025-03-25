# Edge Case
if (len(t) > len(s)):
    return ""
# Build necessary member
missing = len(t)
freq = defaultdict(int)
for c in t:
    freq[c] += 1
lmin = 0
rmin = 0
# Sliding Window
l = 0
for r in range(len(s)):
    c = s[r]
    freq[c] -= 1
    if freq[c] >= 0:
        missing -= 1
    if missing == 0:
        while l <= r: # Shrink until weve added too many
            add_char = s[l]
            freq[add_char] += 1
            if freq[add_char] > 0:
                missing += 1
            if freq[add_char] == 1 and missing == 1: # Weve reached a critical point
                if (lmin == 0 and rmin == 0) or r - l  < rmin - lmin:
                    lmin, rmin = l, r + 1
                l += 1
                break
            l += 1
if lmin == 0 and rmin == 0:
    return ""
return s[lmin:rmin]    
