# Solved the top-k-frequent-elements challenge on leetcode, link: https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newset = set(nums)
        dictui = {}
        newlist = []
        for i in newset:
            length = nums.count(i)
            dictui.update({str(i):length})
        for i in range(0, k):
            most_freq = max(dictui.items(), key=lambda x: x[1])[0]
            newlist.append(int(most_freq))
            del dictui[most_freq]
        return newlist
