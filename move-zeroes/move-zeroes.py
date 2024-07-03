class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_p = 0
        r_p = 0
        for i in range(len(nums)):
            if nums[r_p] == 0:
                r_p += 1
            else:
                temp: int = nums[l_p]
                nums[l_p] = nums[r_p]
                nums[r_p] = temp
                l_p += 1
                r_p += 1
        