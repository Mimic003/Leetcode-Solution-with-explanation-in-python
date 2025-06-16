# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         b=[]
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]-nums[j]==k or nums[j]-nums[i]==k:
#                     a=[nums[i],nums[j]]
#                     a.sort()
#                     if a not in b:
#                         b.append(a)
#         return len(b)

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        ans = 0
        numToIndex = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            target = num + k
            if target in numToIndex and numToIndex[target] != i:
                ans += 1
                del numToIndex[target]
             
        return ans