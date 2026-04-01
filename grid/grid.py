def gridChallenge(grid):
    # Sort each row
    sorted_grid = ["".join(sorted(row)) for row in grid]
    # Zip to get columns
    for col in zip(*sorted_grid):
        if list(col) != sorted(col):
            return "NO"
    return "YES"
