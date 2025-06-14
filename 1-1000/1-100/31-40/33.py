class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target not in nums:
            return -1
        
        cnt=0
        for i in nums:
            if i != target:
                cnt+=1
            else:
                return cnt