def nextGreatestLetter(letters: list[str], target: str) -> str:
  left, right = 0, len(letters) - 1

  last_seen = -1
  while left <= right:
    mid = left + (right - left) // 2

    if letters[mid] > target:
      last_seen = mid
      right = mid - 1
    else:
      left = mid + 1

  if letters[last_seen] > target:
    return letters[last_seen]
  return letters[0]


# print(nextGreatestLetter(["b", "d", "g"], "c"))
'''
Happy Case:
f(["b", "d", "g"], "a") => "b"

Edge Case:
f(["x", "x", "y"], "z") => "x"
f(["a", "b"], a) => "b"
f(["b", "d", "g"], "c") => "d"

Plan (BS):
- initialize the left and right pointers at 0, and len(lst) - 1
- while left <= right
  calculate the mid with left + (right - left) // 2
  if lst[mid] > target
    update right to mid - 1
  else 
    update left to mid + 1
- if lst[mid] > target:
    return lst[mid]
- return lst[0]

Review:
time: O(log n)
space: O(1)
'''

