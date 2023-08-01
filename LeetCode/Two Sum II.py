# Solved the Two Sum II - Input Array Is Sorted challenge, link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leng = len(numbers)
        set1 = set()
        for i in numbers:
            if i not in set1:
                for x in range(leng):
                    if i + numbers[x] == target:
                        if numbers[x] != i:
                            print(i + numbers[x],i)
                            res = [numbers.index(i)+1, x+1]
                            return res
                        else:
                            res = [numbers.index(i)+1, x+2]
                            return res
                set1.add(i)
