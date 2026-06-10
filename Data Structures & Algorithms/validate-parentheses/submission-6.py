class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # i can do a for loop over all of them and then have if { or ( or [ then
        # push it to stack, then pop whenever i get ), ], } and compare index i to
        #len(stack)-i of the list

        # iterate through whole one
        # if get an opening one, append to stack. if see one of the closing ones, either confirm
        # match with pop value or return false

        for i in range(len(s)):
            if (s[i] == "(" or s[i] == "[" or s[i] =="{"):
                stack.append(s[i])
            elif ((s[i] == ")") or (s[i] == "]") or (s[i] =="}")):
                if len(stack) == 0:
                    return False
                elif ((stack[-1] == '{' and s[i] == '}') or
                     (stack[-1] == '(' and s[i] == ')') or
                     (stack[-1] == '[' and s[i] == ']')):
                    
                    stack.pop()
                    
                else:
                    return False

        return (len(stack) == 0)
                