class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        target=sorted(s1)
        for i in range(len(s2)-n+1):
            if sorted(s2[i:i+n])==target:
                return True
        return False

        
        