class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRightElem = -1
        for i in range(len(arr) - 1, -1, -1):
            currentElem = arr[i]
            arr[i] = maxRightElem
            maxRightElem = max(currentElem, maxRightElem)
            
        return arr