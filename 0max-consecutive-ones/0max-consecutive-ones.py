class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxConsecutive = 0
        currentConsecutive = 0
        for num in nums:
            if num == 1:
                currentConsecutive += 1
            else:
                maxConsecutive = currentConsecutive if currentConsecutive > maxConsecutive else maxConsecutive
                currentConsecutive = 0
        maxConsecutive = currentConsecutive if currentConsecutive > maxConsecutive else maxConsecutive

        return maxConsecutive