def searchRange(nums: list[int], target: int) -> list[int]:
   # Write your code here
  positions: list[int] = []
  left, right = 0, len(nums) - 1

  while left <= right:
      mid: int = left + (right - left) // 2
      if nums[mid] >= target:
          right = mid - 1
      else:
          left = mid + 1

  if nums[left] == target:
      positions.append(left)
  else:
      positions.append(-1)

  left, right = 0, len(nums) - 1
  while left <= right:
      mid: int = left + (right - left) // 2
      if nums[mid] <= target:
          left = mid + 1
      else:
          right = mid - 1
  if nums[right] == target:
      positions.append(right)
  else:
      positions.append(-1)
  return positions
print(searchRange([5,7,7,8,8,8,10], 8))