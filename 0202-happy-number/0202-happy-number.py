class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set() # Dùng set để lưu các số đã xuất hiện
        
        while n != 1:
            # Tính tổng bình phương các chữ số
            n = sum(int(digit) ** 2 for digit in str(n))
            
            # Nếu n đã xuất hiện trước đó, tức là bị lặp vô tận
            if n in visited:
                return False
            
            # Nếu chưa, thêm n vào danh sách đã thăm
            visited.add(n)
            
        return True