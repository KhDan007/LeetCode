class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l_p: int = 0
        r_p: int = 0
        while l_p < len(nums) and r_p < len(nums):
            if nums[l_p] % 2 == 0:
                l_p += 1
                continue
            if nums[r_p] % 2 == 0 and r_p > l_p:
                temp: int = nums[l_p]
                nums[l_p] = nums[r_p]
                nums[r_p] = temp
                l_p += 1
                r_p += 1
            else:
                r_p += 1
        return nums