class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n, m = len(s), len(t)
        
        while i < n and j < m:
            # Nếu ký tự khớp nnhau nhích con trỏ của chuỗi con s lên
            if s[i] == t[j]:
                i += 1
            # Luôn luôn nhích con trỏ của chuỗi gốc t lên
            j += 1
            
        # Nếu đi hết được chuỗi s (i bằng độ dài s) thì nó là subsequence
        return i == n