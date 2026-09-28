class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            remainder = target - num

            try:
                remainder_ind = nums[index+1:].index(remainder)
                return [index, remainder_ind + index +1]
            except:
                continue
