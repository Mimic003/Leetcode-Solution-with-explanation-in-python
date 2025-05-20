class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l=0
        ml=0

        for r in range(len(s)):
            while s[r]in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ml=max(ml, r-l+1)
        return ml

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         m=0
#         for i in range(len(s)):
#             cnt=1
#             for j in range(1, len(s)):
#                 if s[i]!=s[j]:
#                     cnt+=1
#                 else:
#                     m=max(m,cnt)
#         if s != "":
#             return m
#         else:
#             return 0     