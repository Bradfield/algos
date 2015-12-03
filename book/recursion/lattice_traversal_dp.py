
def num_paths_dp(height, width):
    memo = [[1] * (width + 1) for _ in range(0, height + 1)]
    for i, row in enumerate(memo):
        for j, _ in enumerate(row):
            if i == 0 or j == 0:
                continue
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]
