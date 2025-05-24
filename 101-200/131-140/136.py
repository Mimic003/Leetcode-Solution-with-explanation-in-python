class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            cnt=0
            for j in nums:
                if i==j:
                    cnt+=1
            if cnt==1:
                return i