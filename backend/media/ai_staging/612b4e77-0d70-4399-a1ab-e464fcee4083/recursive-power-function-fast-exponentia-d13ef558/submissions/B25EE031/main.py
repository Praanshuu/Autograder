def recursion_power(x, n):
    # Base case
    if n == 0:
        return 1.0
    
    # Handle negative powers
    if n < 0:
        return 1 / recursion_power(x, -n)
    
    # Divide step
    half = recursion_power(x, n // 2)
    
    # Conquer step
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
