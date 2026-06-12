class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we are going to do two pointers, one at idx = 0 and one at idx = len-1
        # while left idx

        # consider both odd and even, probrobally not an issue. needs to be at least 1 -- already
        # considered

        # failed once, it can be case insensative. how should i do this? i might also need
        # to consider spacing.
        left = 0
        right = len(s)-1

        while (left < right):

            if ((s[right].isalnum() and s[left].isalnum()) and
            (s[left].lower() == s[right].lower())):
                left += 1
                right -= 1
            elif (not(s[right].isalnum())):
                right -= 1
            elif  (not(s[left].isalnum())):
                left += 1
            
            else:
                return False


        return True