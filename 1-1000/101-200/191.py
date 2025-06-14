# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         ans=0

#         for i in range(32):
#             if (n >> i) & 1:
#                 ans+=1
#         return ans

class Solution:
    def hammingWeight2(self, n: int) -> int:
        ans=0
        while n:
            ans+=1
            n&=n-1