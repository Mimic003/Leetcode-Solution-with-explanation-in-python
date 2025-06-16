# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         for i in range(len(nums)-2):
#             if nums[i]<nums[i+1]<nums[i+2]:
#                 return True
#         return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f=float('inf')
        s=float('inf')

        for num in nums:
            if num<=f:
                f=num
            elif num<=s:
                s = num
            else:
                return True
        
        return False