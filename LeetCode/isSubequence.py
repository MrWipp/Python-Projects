"""Solved the is subsequence challenge (easy) in 1 hour beats(99%) and without the use of any help, link: https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not)."""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        else:
            s2 = ""
            for i in t:
                if i in s:
                    s2+=i
                    if s2.count(i) > s.count(i):
                        s2 = s2.replace(i,"",1)
                if s in s2:
                    return True
            return False
