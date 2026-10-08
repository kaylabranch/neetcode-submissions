class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if bool(s) and bool(t) and len(s) != len(t):
            return False
            
        return all(a == b for a, b in zip(sorted(s), sorted(t)))