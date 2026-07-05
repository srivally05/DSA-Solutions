class Solution:
    def isRectangleOverlap(self, x: List[int], y: List[int]) -> bool:
        return not(x[2]<=y[0] or y[2]<=x[0] or x[3]<=y[1] or y[3]<=x[1] )
        
