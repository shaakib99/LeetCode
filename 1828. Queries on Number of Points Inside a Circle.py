class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        import math
        output = []
        for q in queries:
            count = 0
            for p in points:
                distance = math.sqrt((q[0] - p[0])**2  + (q[1] - p[1])**2)
                if distance <= q[2]: count += 1
            output.append(count)
        return output