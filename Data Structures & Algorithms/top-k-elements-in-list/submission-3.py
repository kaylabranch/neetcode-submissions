class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for item in nums:
            my_dict[item] = my_dict.get(item, 0) + 1

        dict_sorted = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:k]
        dict_keys = [x[0] for x in dict_sorted]
        
        return dict_keys