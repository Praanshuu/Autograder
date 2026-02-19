def findMissingNumber(arr):
  count = 0
  arr.sort()
  for i in arr:
    if i==count:
      count = count+1
    else:
      return count
  return count

      