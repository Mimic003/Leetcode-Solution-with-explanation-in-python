# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         s = [nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
#         c=0
#         for i in s:
#             if sum(i)==k:
#                 c+=1
#         return c


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a = 0
        b = 0
        c = collections.Counter({0: 1})
        for num in nums:
            b += num
            a += c[b - k]
            c[b] += 1
        return a