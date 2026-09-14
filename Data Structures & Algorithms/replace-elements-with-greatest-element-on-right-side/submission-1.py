class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #initial   max = -1
        #reversse iteration
        #new max = max(oldmax, arr[i])
        rightMax = -1

        #start at the last value in the array, iterate in reverse order, stop once we get to beginning of array
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr




        