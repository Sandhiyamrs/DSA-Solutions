def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for n in nums:
        current_sum += n
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum


# Example run
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum:", max_subarray_sum(arr))
