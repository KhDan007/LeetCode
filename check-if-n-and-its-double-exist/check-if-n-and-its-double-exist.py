class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
                j += 1
            i += 1
        return False