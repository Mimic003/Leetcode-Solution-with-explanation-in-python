import sys

nums = [int(x) for x in sys.argv[1].split(',')]

def nextPermutation(nums):
	n=len(nums)

	i=n-2
	while i>=0:
		if nums[i]<nums[i+1]:
			break
		i-=1
	if i>=0:
		for j in range(n-1,i,-1):
			if nums[j]>nums[i]:
				nums[i],nums[j]==nums[j],nums[i]
				break
	def reverse(nums,l,r):
		while l<r:
			nums[l],nums[r]=nums[r],nums[l]
			l+=1
			r-=1

	return reverse(nums, i+1,len(nums)-1)
	

print(",".join(map(str, nextPermutation(nums))))