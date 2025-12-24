def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area
