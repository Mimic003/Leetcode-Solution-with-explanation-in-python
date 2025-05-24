# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         w=0
#         for i in range(len(height)-1):
#             for j in range(i+1,len(height)):
#                 m=(j-i)
#                 n=min(height[i],height[j])
#                 m*=n
#                 w=m if m>w else w
#         return w

class Solution:
  def maxArea(self, height: list[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      ans = max(ans, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return ans