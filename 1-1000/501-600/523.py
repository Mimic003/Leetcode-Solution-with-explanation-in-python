# class Solution:
#     def checkSubarraySum(self, nums: list[int], k: int) -> bool:
#         return sum(nums)%k==0 

class Solution:
  def checkSubarraySum(self, nums: list[int], k: int) -> bool:
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += num
      if k != 0:
        prefix %= k
      if prefix in prefixToIndex:
        if i - prefixToIndex[prefix] > 1:
          return True
      else:
        prefixToIndex[prefix] = i

    return False