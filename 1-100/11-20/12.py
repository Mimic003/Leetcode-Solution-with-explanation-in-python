class Solution:
    def intToRoman(self, num: int) -> str:
        v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        r=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        s=''
        i=0
        while num>0:
            for _ in range(num//v[i]):
                s+=r[i]
                num-=v[i]
            i+=1
        return(s)