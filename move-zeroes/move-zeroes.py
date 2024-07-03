class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_count = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zero_count += 1
                continue
            i += 1
        for i in range(zero_count):
            nums.append(0)
        