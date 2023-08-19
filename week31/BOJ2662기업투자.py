n, m = map(int, input().split())
invest = [[0 for _ in range(m + 1)]]

for _ in range(n):
    invest.append(list(map(int, input().split())))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

pos = [[[0 for _ in range(m+1)] for _ in range(m + 1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):

        dp[i][j] = max(dp[i][j-1], invest[i][j])
        if dp[i][j] == invest[i][j]:
            pos[i][j][j] = i
        else:
            pos[i][j] = pos[i][j-1].copy()
            
        for k in range(1, i+1):
            if dp[i][j] < dp[k][j-1] + invest[i-k][j]:
                dp[i][j] = dp[k][j-1] + invest[i-k][j]
                pos[i][j] = pos[k][j-1].copy()
                pos[i][j][j] = i-k
                
print(dp[-1][-1])
print(*pos[-1][-1][1:])