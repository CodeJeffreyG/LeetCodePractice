class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        i = 0
        j = 0
        subStringLength = 0
        charSet = set()
        #check if j is in set... if its not add it then increase by 1
        #keep itterating until j is in set or length of string..
        #if j is in set remove current i... then itterate i by 1.. keep going until substring is valid..
        #zxyzxyz
        #  i j
        #{x,y,z}

        
        
        while j < len(s):
            
            
            if s[j] not in charSet:
                charSet.add(s[j])
                j += 1
                subStringLength = max(subStringLength, j - i)
            else:
                charSet.remove(s[i])
                i += 1
        return subStringLength

        