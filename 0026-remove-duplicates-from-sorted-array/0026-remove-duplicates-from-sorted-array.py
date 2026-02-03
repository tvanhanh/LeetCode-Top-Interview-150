# Bài 26: Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        if not nums:
            return 0
        
    
        insert_index = 1
        
      
        for i in range(1, len(nums)):
         
            if nums[i] != nums[i - 1]:
                # Nếu khác nhau thi tìm thấy 1 số mới không trùng
                # Chép số mới này vào vị trí insert_index
                nums[insert_index] = nums[i]
                # Nhích vị trí chèn lên để chờ số tiếp theo
                insert_index += 1
        
     
        return insert_index