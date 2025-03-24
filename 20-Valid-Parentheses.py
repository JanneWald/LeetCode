def isValid(self, s):
    stack = []
    push = set(["(", "{", "["])
    open = {")":"(", "}" : "{","]":"["}
    for c in s:
        if c in push:
            stack.append(c)
        elif len(stack) == 0:
            return False
        elif stack.pop() != open[c]:
            return False
    return len(stack) == 0
