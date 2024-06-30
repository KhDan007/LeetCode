class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] <= arr[0]:
            return False
        is_increasing = True
        prev_num = arr[1]
        i = 2
        while i < len(arr):
            if arr[i] == prev_num:
                return False
            if is_increasing and arr[i] < prev_num:
                is_increasing = False
            elif not is_increasing and arr[i] > prev_num:
                return False
                
            prev_num = arr[i]
            i += 1
        if is_increasing:
            return False
        return True
                