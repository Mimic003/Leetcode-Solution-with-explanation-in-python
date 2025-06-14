class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        return (nums[k-1])
        