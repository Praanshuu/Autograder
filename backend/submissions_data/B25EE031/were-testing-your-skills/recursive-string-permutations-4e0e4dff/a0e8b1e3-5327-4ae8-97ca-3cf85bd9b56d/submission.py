def permute_recursive(s):
    s = sorted(s)          # ensure lexicographic order
    result = []
    
    def backtrack(index):
        if index == len(s):
            result.append("".join(s))
            return
        
        for i in range(index, len(s)):
            s[index], s[i] = s[i], s[index]
            backtrack(index + 1)
            s[index], s[i] = s[i], s[index]
    
    backtrack(0)
    return result
