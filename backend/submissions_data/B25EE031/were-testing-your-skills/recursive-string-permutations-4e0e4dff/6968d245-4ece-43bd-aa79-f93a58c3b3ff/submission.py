def reverse_string(s):
    result = []
    s = sorted(s)  # Ensure lexicographic order
    
    def backtrack(index):
        # Base case
        if index == len(s):
            result.append("".join(s))
            return
        
        for i in range(index, len(s)):
            # Swap
            s[index], s[i] = s[i], s[index]
            
            # Recurse
            backtrack(index + 1)
            
            # Backtrack (undo swap)
            s[index], s[i] = s[i], s[index]
    
    backtrack(0)
    return sorted(result)
