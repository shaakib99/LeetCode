class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """

    '''
    * To make permutation we need to count each character in s
    * Check if each character in pair or allow max 1 max odd number of character
    '''
    def can_permute_palindrome(self, s: str) -> bool:
        from collections import defaultdict

        counter = defaultdict(int)
        for c in s: counter[c] += 1

        maxOdd = 0
        for k, v in counter.items():
            mod = v % 2
            if not mod and maxOdd == 1: return False
            if mod: maxOdd += 1
        return True