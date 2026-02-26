class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      
        map_st = {}
        map_ts = {}

        for char_s, char_t in zip(s, t):
            # Kiểm tra ánh xạ từ s sang t
            if char_s in map_st and map_st[char_s] != char_t:
                return False
            
            # Kiểm tra ngược lại từ t sang s (đảm bảo tính 1-1)
            if char_t in map_ts and map_ts[char_t] != char_s:
                return False
            
            map_st[char_s] = char_t
            map_ts[char_t] = char_s
            
        return True
        