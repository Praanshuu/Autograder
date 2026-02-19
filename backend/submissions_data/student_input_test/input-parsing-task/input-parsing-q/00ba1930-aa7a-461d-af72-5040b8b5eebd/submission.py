def sum_even_numbers(nums):
    # If nums is dynamic input string, it should be parsed to list by runner
    # If not parsed, this will raise TypeError
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total