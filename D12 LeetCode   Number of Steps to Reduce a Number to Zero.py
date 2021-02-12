class Solution:
    def numberOfSteps (self, num: int) -> int:
        s=0
        while num>0:
            if num%2==0:
                num=num//2
            else:
                num=num-1
            s=s+1
        return s
