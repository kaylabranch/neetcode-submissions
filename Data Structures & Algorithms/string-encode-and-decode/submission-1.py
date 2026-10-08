class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index('#', i)           # find the end of the length prefix
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length            # jump past this string
        return result