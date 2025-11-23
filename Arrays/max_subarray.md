# 📌Maximum Subarray Sum – Kadane’s Algorithm

## Problem Statement
Given an integer array, find the contiguous subarray with the largest sum and return its sum.

##📘 Example
-Input: [-2,1,-3,4,-1,2,1,-5,4]
-Output: 6

-Explanation:
The subarray [4,-1,2,1] has the maximum sum = 6.

## 🧠Approach
We iterate through the array and keep track of:
---current_sum → running sum of subarray
---max_sum → highest sum found so far
-If current_sum becomes negative, we reset it to 0 because negative sums reduce the total.

## 🧩 Python Solution
def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for n in nums:
        current_sum += n
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum


## Time: O(n)
## Space: O(1)
