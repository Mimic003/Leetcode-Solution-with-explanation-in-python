#class Solution:
# def containDuplicates(nums):
# 	for i in range(len(nums)-1):
# 		for j in range(i+1,len(nums)):
# 			if nums[i]==nums[j]:
# 				return True
# 	return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))