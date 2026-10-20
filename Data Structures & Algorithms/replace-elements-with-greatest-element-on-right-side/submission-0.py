class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for out_index in range(len(arr) - 1):                       # ignore last item
            maximum = arr[out_index + 1]
    
            for in_index in range(out_index + 1, len(arr)):
                if arr[in_index] > maximum:
                    maximum = arr[in_index]

            arr[out_index] = maximum

        arr[-1] = -1

        return arr     
        