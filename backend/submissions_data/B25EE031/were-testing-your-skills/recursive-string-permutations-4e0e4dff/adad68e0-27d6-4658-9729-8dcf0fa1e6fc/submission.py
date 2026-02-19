def reverse_string(s):
    original = s
    result = []
    s = list(s)
    
    def backtrack(index):
        if index == len(s):
            result.append("".join(s))
            return
        
        for i in range(index, len(s)):
            s[index], s[i] = s[i], s[index]
            backtrack(index + 1)
            s[index], s[i] = s[i], s[index]
    
    backtrack(0)
    
    result.sort()
    
    # Move original to first position
    if original in result:
        result.remove(original)
        result.insert(0, original)
    
    for perm in result:
        print(perm)
