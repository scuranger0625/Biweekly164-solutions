class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # 中途存輸入（題目要求）
        drunepalix = s

        n = len(s)
        Z0 = s.count('0')
        if Z0 == 0:
            return 0
        if k == n:
            return 1 if Z0 == n else -1
        if (k & 1) == 0 and (Z0 & 1) == 1:
            return -1

        INF = 10**18
        dist = [INF] * (n + 1)
        dist[Z0] = 0

        # 只修補不同奇偶的位置；其餘保持 self-loop，利於 O(1) 判斷
        def build_next(parity: int):
            nxt = list(range(n + 3))
            for i in range(parity ^ 1, n + 1, 2):
                nxt[i] = i + 1
            nxt[n + 1] = n + 1
            nxt[n + 2] = n + 2
            return nxt

        next_even = build_next(0)
        next_odd  = build_next(1)

        # 迭代式 find（帶路徑壓縮）
        def find(nxt, x: int) -> int:
            while nxt[x] != x:
                nxt[x] = nxt[nxt[x]]
                x = nxt[x]
            return x

        # 標記已訪（跳到同奇偶下一個）
        def erase(nxt, x: int):
            nxt[x] = find(nxt, x + 2)

        # 起點移除
        if (Z0 & 1) == 0:
            erase(next_even, Z0)
        else:
            erase(next_odd, Z0)

        q = deque([Z0])
        append = q.append
        popleft = q.popleft
        dist_arr = dist  # 綁成區域變數減少層級查找

        while q:
            Z = popleft()
            d = dist_arr[Z]
            O = n - Z

            tl = 0 if k <= O else k - O
            tr = k if k <= Z else Z
            if tl > tr:
                continue

            L = Z + k - (tr << 1)
            R = Z + k - (tl << 1)
            if L < 0: L = 0
            if R > n: R = n

            parity = (Z + k) & 1
            nxt = next_even if parity == 0 else next_odd

            i = L if (L & 1) == parity else L + 1
            i = find(nxt, i)
            while i <= R:
                if dist_arr[i] == INF:
                    dist_arr[i] = d + 1
                    append(i)
                erase(nxt, i)
                i = find(nxt, i)

        return -1 if dist_arr[0] == INF else dist_arr[0]
