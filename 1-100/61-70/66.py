from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l= len(digits)
        for i in range(l-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1] + digits