def flood_fill(image, sr, sc, new_color):
    start_color = image[sr][sc]

    if start_color == new_color:
        return image

    def dfs(r, c):
        if (r < 0 or c < 0 or 
            r >= len(image) or c >= len(image[0]) or 
            image[r][c] != start_color):
            return

        image[r][c] = new_color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image
