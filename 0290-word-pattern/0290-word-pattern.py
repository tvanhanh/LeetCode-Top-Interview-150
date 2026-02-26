class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() # Tách chuỗi s thành mảng các từ
        
        # kiểm tra số lượng từ của mảng r so sánh với mẫu
        if len(pattern) != len(words):
            return False
            
        map_pw = {} 
        map_wp = {} 

        for p, w in zip(pattern, words):
            # Kiểm tra chiều đi: Ký tự p phải luôn đi với từ w
            if p in map_pw and map_pw[p] != w:
                return False
            # Kiểm tra chiều về: Từ w phải luôn đi với ký tự p
            if w in map_wp and map_wp[w] != p:
                return False
                
            map_pw[p] = w
            map_wp[w] = p
            
        return True
        