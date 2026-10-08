class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for item in strs:
            # sort item
            item_sorted = "".join(sorted(item))

            # if item in my_dict, push to that key's array
            my_dict.setdefault(item_sorted, []).append(item)

        # return set items as array
        return list(my_dict.values())