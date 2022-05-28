from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initial solution
        # return Counter(s) == Counter(t) 
        
        if len(s) != len(t):
            return False
        
        counter = defaultdict(int)
        for c1, c2 in zip(s, t):
            counter[c1] += 1
            counter[c2] -= 1
        
        for count in counter:
            if counter[count] != 0:
                return False
            
        return True