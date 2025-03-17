def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        letters = [0] * 26
        
        for c in word:
            letterIndex = ord(c) - ord('a')
            letters[letterIndex] += 1
            
        anagramKey = tuple(letters)
        anagrams[anagramKey].append(word)

    return anagrams.values()
