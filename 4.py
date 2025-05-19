class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l=len(nums1)
        if l%2==0:
            a = l//2
            b = a-1
            return (nums1[a]+nums1[b])/2
        else:
            return nums1[l//2]