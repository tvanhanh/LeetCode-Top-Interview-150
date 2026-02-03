class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Bỏ qua ký tự bên trái nếu không phải là chữ hoặc số
            while left < right and not s[left].isalnum():
                left += 1
            # Bỏ qua ký tự bên phải nếu không phải là chữ hoặc số
            while left < right and not s[right].isalnum():
                right -= 1
            
            # So sánh hai ký tự sau khi đã chuyển về chữ thường
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
        