class Solution:
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        '''
        STEP #1
        *. Check if string difference is more than 2
        * if difference is more than 2 we can return False since we need more than 2 remove or add
        * Take two pointer p1, p2
        * if s[p1] == t[p2], we need to update p1 and p2 simultaneously
        * if s[p1] != t[p2] 
            check if len(s) == len(t) which confirms we need to change a character
            else we have to update p1 or p2 conditionally. Which confirms we need to remove or add character
        '''
        if abs(len(s) - len(t)) > 1: return False
        p1 = 0
        p2 = 0
        maxChange = 0

        while p1 < len(s) or p2 < len(t):
            ts = s[p1] if p1 < len(s) else ""
            tt = t[p2] if p2 < len(t) else ""

            if ts != tt:
                if maxChange == 1: return False
                maxChange += 1
                if len(s) == len(t): 
                    p1 += 1
                    p2 += 1
                else:
                    if len(s) > len(t): p1 += 1
                    else: p2 += 1  
            else:
                p1 += 1
                p2 += 1 

        return maxChange == 1