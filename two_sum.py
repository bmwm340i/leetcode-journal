# ==========================================================
# LeetCode 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution.
"""

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]
