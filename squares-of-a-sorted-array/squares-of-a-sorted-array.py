class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = list(map(lambda x: x * x, nums))
        squares.sort()
        return squares