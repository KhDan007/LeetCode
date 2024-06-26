class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digits_count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_digits_count += 1
        return even_digits_count
            