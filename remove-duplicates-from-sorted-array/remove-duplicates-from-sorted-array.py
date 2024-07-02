class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        nums[:] = [x for x in nums if x not in seen and not seen.add(x)]
        return len(nums)
            