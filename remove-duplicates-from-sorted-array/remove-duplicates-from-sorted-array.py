class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        helper_tuple = set()
        i = 0
        while i < len(nums):
            if nums[i] not in helper_tuple:
                helper_tuple.add(nums[i])
                i += 1
                continue
            nums.pop(i)
        return len(nums)
            
            