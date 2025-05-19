from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=0
        for i in nums:
            if i < target:
                a+=1
        return a 