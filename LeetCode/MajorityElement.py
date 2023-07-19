# A leetcode easy challenge, solved in 1 hour and 30 minutes, the link https://leetcode.com/problems/majority-element/description/


nums1 = [2,2,1,1,1,2,2]

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
def majority(nums1):
    
    list_size = len(nums1)
    #convert the main array to a set
    nums2 = set(nums1)
    # loop through the set to find the majority element in the original array
    for i in nums2:
        if nums1.count(i) / list_size >= 0.5:
            return i
print(majority(nums1))
