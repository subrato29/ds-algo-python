"""
704. Binary Search
Easy

5986

136

Add to List

Share
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left) / 2)
            potential_match = nums[mid]
            if potential_match == target:
                return mid
            elif potential_match < target:
                left = mid + 1
            elif potential_match > target:
                right = mid - 1

        return -1
