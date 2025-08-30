class Solution:
    def score(self, cards: List[str], x: str) -> int:
        # 中途暫存輸入（題目要求）
        brivolante = cards

        # 僅保留含 x 的卡；少於 2 張無法配對
        has_x = [c for c in cards if x in c]
        if len(has_x) < 2:
            return 0

        left  = [0] * 10 # 三類計數：
        right = [0] * 10 # left[i]  代表 "x?"，另一個字母是 chr(ord('a')+i)
        doubles = 0      # right[i] 代表 "?x"，另一個字母是 chr(ord('a')+i)
        base = ord('a')  # doubles   代表 "xx"

        for s in has_x:
            a, b = s[0], s[1]
            if a == x and b == x:
                doubles += 1
            elif a == x and b != x:      # "x?"
                left[ord(b) - base] += 1
            elif b == x and a != x:      # "?x"
                right[ord(a) - base] += 1
            # 其他情況不會發生（因為事先過濾 has_x）

        # 幫手：在同一側，最多能用「不同字母」配出多少對
        def max_pairs_diff(counts: List[int]) -> int:
            total = sum(counts)
            if total < 2:
                return 0
            m = max(counts)
            # 不能用相同字母互配 → 上限是 min(total//2, total - m)
            return min(total // 2, total - m)

        L_pairs_max = max_pairs_diff(left)
        R_pairs_max = max_pairs_diff(right)
        Pmax = L_pairs_max + R_pairs_max

        S = sum(left) + sum(right)   # 單張總數（不含 "xx"）
        D = doubles

        # 若 "xx" 比單張還多，全部單張都可被 "xx" 吸收
        if D >= S:
            return S

        # 否則，先做 P 個左右各自的配對，再用 "xx" 吸剩下的單張
        # 最佳 P 取在邊界：讓剩下的單張數 S-2P ≈ D
        P = min(Pmax, (S - D) // 2)
        leftover = S - 2 * P
        extra = min(D, leftover)

        return P + extra
