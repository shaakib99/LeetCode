'''
STEP #1 SORTING + SLIDING WINDOW
space complexity 1
time complexity len(s1) * log(len(s1)) + len(s2) * len(s1) * log(len(s1))
* sort s1
* Run a sliding window of constant size of s1 on s2.
* sort the window and compare with s1

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        p1 = 0
        p2 = 0
        while p2 < len(s2):
            if p2 - p1 + 1 == len(s1):
                if sorted(s2[p1: p2 + 1]) == s1: return True
                p1 += 1
            p2 += 1
        return False
'''
STEP #2 HASHMAP + SLIDING WINDOW
space complexity len(s1) + len(s2)
time complexity len(s1) + len(s2) * 26

* count number of individual character in s1.
* Run a sliding window of constant size of s1 on s2.
* Take a counter, which will be responsible for counting number of characters in in a fix window size.
'''


class Solution:

    def checkPerm(self, counter1:dict, counter2: dict):
        for k, v in counter1.items():
            if v != counter2[k]: return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        s1Counter = defaultdict(int)
        for s in s1:
            s1Counter[s] += 1

        p1 = 0
        p2 = 0
        s2Counter = defaultdict(int)
        while p2 < len(s2):
            s2Counter[s2[p2]] += 1
            if p2 - p1 + 1 == len(s1):
                if self.checkPerm(s1Counter, s2Counter): return True
                s2Counter[s2[p1]] -= 1
                p1 += 1
            p2 += 1
        return False