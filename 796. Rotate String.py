class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        arr = [c for c in s]
        for _ in range(len(s)):
            for i in range(len(arr) - 1):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if ''.join(arr) == goal: return True
        return False