class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the basic way of doing this is to go through all of 1 and add their
        # characters O(n^2). can also do this with key value pairs in a hash
        # map, this allows for O(n) solving. 

        # make hashmap of s and put the number of characters
        s_hash = {}
        for char in s: 
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1
        
        # make hashmap of s and put the number of characters
        t_hash = {}
        for char in t: 
            if char in t_hash:
                t_hash[char] += 1
            else:
                t_hash[char] = 1

        return t_hash == s_hash



        # when using == to compare hashmaps, order does not matter

