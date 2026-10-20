class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for index in range(len(nums)):
                ans.append(nums[index])

        return ans

        