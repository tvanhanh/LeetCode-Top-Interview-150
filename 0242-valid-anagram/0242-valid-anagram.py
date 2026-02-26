class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Nếu độ dài khác nhau thì chắc chắn không phải đảo chữ
        if len(s) != len(t):
            return False
        
        # Dùng một Dictionary để đếm số lần xuất hiện của mỗi ký tự
        count = {}

        # Duyệt qua chuỗi s để cộng dồn số lượng ký tự
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Duyệt qua chuỗi t để trừ bớt số lượng ký tự
        for char in t:
            # Nếu ký tự trong t không có trong s hoặc đã bị trừ hết (về 0)
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True