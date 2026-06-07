class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(sorted(t))
        print(sorted(s))
        return sorted(s) == sorted(t)
