def activity_selection(start, end):
    activities = sorted(zip(start,end), key=lambda x: x[1])
    res = [activities[0]]
    last_end = activities[0][1]

    for s,e in activities[1:]:
        if s >= last_end:
            res.append((s,e))
            last_end = e
    return res

# Example usage
start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
print("Output:", activity_selection(start,end))
