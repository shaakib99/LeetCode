'''
STEP # 1
* using n extra space, n runtime
* using string
'''

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        chars.append(" ")
        count = 1
        for c in chars:
            if len(s) and s[-1] == c: count += 1
            else:
                if count > 1: s += str(count)
                s += c
                count = 1
        return len(s) - 1

'''
STEP #2 LEETCODE SOLUTION
* using O(1) space n runtime
* using first pointer slow pointer
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = 0
        p2 = 0
        count = 0
        chars.append(" ") # Added extra space to set count for last character
        while p2 < len(chars):
            if chars[p1] != chars[p2]:
                p1 += 1 # Need to increase p1 by 1 step to write the number on the next index
                if count > 1:
                    temp = str(count)
                    for c in temp:
                        chars[p1] = c
                        p1 += 1
                chars[p1] = chars[p2]
                count = 1 # Set count = 1, because we found a new character at p2
            else: count += 1
            p2 += 1
            
        l = len(chars)
        while p1 < l:
            chars.pop()
            l -= 1
        return chars