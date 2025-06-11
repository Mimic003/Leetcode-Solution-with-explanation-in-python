class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = []     # Remove the extra 0s from the end of nums1
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        return nums1