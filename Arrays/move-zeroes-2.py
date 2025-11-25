def move_zeroes(nums):
    insert_pos = 0

    for n in nums:
        if n != 0:
            nums[insert_pos] = n
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums
