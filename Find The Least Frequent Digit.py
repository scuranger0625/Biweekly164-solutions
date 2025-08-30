class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # 把 n 轉成字串，注意要取絕對值，避免負號
        s = str(abs(n))
        #  Counter 統計每個數字出現次數
        freq = Counter(s)
        # 找出最小出現次數
        min_cnt = min(freq.values())
        # 把所有出現次數等於 min_cnt 的數字挑出來，轉成整數後取最小
        candidates = [int(d) for d, c in freq.items() if c == min_cnt]
        return min(candidates)
