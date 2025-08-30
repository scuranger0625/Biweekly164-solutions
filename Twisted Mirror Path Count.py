MOD = 10**9 + 7

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 題目要求：中途存輸入到變數 vornadexil
        vornadexil = grid

        # 小工具：模擬「從某方向走進一個位置」後，最終落腳點
        # dir = 0 表示從左往右進來，dir = 1 表示從上往下進來
        def move(i: int, j: int, dir: int):
            while 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                if dir == 0:  # 往右撞到鏡子 → 轉向下
                    i += 1
                    dir = 1
                else:         # 往下撞到鏡子 → 轉向右
                    j += 1
                    dir = 0
            # 回傳落腳點，如果越界就標記 None
            if not (0 <= i < m and 0 <= j < n):
                return None
            return (i, j)

        # DP 初始化
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # 遍歷整個 grid
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                # 嘗試往右
                if j + 1 < n:
                    nxt = move(i, j + 1, 0)
                    if nxt:
                        ni, nj = nxt
                        dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD

                # 嘗試往下
                if i + 1 < m:
                    nxt = move(i + 1, j, 1)
                    if nxt:
                        ni, nj = nxt
                        dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD

        return dp[m-1][n-1]
