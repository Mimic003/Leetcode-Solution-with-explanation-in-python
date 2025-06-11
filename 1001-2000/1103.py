class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        a=[0]*num_people
        give=1
        i=0

        while candies>0:
            current =min(give,candies)
            a[i%num_people]+=current
            candies-=current
            give+=1
            i+=1
        return a