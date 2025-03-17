def encode(self, strs: List[str]) -> str:
    result = ""
    for s in strs:
        result += str(len(s))
        result += "#"
        result += s
    return result

def decode(self, s: str) -> List[str]:        
    result = []
    length = 0
    i = 0
    while i < len(s):
        char = s[i]
        if char != '#':
            length *= 10
            length += int(char)
            i += 1
        else:
            word = s[i + 1:i + length + 1]
            result.append(word)
            i += length + 1
            length = 0
    return result
