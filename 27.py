from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        for i in nums:
            if val!=i:
                nums[cnt]=i
                cnt+=1
        return cnt