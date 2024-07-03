class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        l_p = 0
        r_p = 0
        while r_p < len(nums) and l_p < len(nums):
            if nums[l_p] != val:
                l_p += 1
                r_p += 1
                continue
            if nums[r_p] != val and r_p > l_p:
                temp: int = nums[l_p]
                nums[l_p] = nums[r_p]
                nums[r_p] = temp
                r_p += 1
                l_p += 1
            else:
                r_p += 1
        return l_p