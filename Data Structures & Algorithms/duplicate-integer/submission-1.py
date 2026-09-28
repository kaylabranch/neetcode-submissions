class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        dupe = False

        for num in nums:
            if num in num_set:
                dupe = True
                break
            
            num_set.add(num)
        
        return dupe