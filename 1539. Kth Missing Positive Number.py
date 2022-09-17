class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # a = []
        # for i in range(1, arr[-1] + 1): 
        #     if i not in arr: a.append(i)
        # if len(a) < k: return arr[-1] + k - len(a)
        # return a[k - 1]
    
        if arr[-1] == len(arr): return len(arr) + k
        missing = abs(1 - arr[0])
        if missing >= k: return 1 + k - 1
        
        for i in range(1, len(arr)):
            diff = abs(arr[i - 1] - arr[i])
            if diff != 1: missing += diff - 1
            if missing >= k:
                missing -= diff - 1
                return arr[i - 1] +  k - missing
        return arr[-1] + k - missing
        