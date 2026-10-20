class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearance = {}

        for index in range(len(nums)):
            if nums[index] in appearance:
                appearance[nums[index]] += 1

            else:
                appearance[nums[index]] = 1

        
        for key in appearance:
            if appearance[key] > 1:
                return True

        return False

