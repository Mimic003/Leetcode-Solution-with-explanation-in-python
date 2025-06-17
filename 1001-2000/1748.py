class Solution(object):
    def sumOfUnique(self, nums):
        s=0
        for i in range(len(nums)):
            cnt=0
            for j in nums:
                if j==nums[i]:
                    cnt+=1
            if cnt==1:
                s+=nums[i]
        return s