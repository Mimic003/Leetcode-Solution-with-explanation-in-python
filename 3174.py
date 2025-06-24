class Solution(object):
    def clearDigits(self, s):
        ans=[]

        for i in s:
            if i.isdigit():
                if len(ans)!=0:
                    ans.pop()
            else:
                ans.append(i)

        return ''.join(ans)
        