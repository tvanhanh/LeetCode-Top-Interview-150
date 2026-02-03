# Problem: 27. Remove Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Dùng k để đánh dấu vị trí sẽ chèn số hợp lệ (khác val)
        k = 0
        
        # Chạy i để quét qua cả mảng
        for i in range(len(nums)):
            # Nếu gặp số không phải số cần xóa
            if nums[i] != val:
                # Chép nó đè lên vị trí k hiện tại
                nums[k] = nums[i]
                # Nhích k lên để chờ số tiếp theo
                k += 1
                
        # Trả về k cũng chính là số lượng phần tử còn lại
        return k