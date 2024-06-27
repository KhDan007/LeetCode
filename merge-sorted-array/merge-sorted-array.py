class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - m
        while i > 0:
            nums1.pop()
            i -= 1

        i = len(nums2) - n
        while i > 0:
            nums2.pop()
            i -= 1

        nums1.extend(nums2)
        nums1.sort()