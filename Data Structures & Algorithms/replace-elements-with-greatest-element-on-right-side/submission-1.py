class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for index in range(len(arr) - 1):                       # ignore last item
            arr[index] = max(arr[index + 1:len(arr)])
     
        arr[-1] = -1

        return arr     
        

