# Solved the length of the last word challenge (easy) in 40 minutes, link: https://leetcode.com/problems/length-of-last-word/


"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only."""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = -1
        total = 0
        try:
            for i in s:
                if s[index] != " ":
                    total+=1
                index-=1
                if total > 0 and s[index] == " ":
                    return total
        except:
            s = s.replace(" ", "")
            return len(s)
          
