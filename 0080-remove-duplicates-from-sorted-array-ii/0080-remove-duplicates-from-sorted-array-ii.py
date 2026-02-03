class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for n in nums:
            # Nếu chưa đủ 2 phần tử đầu tiên 
            # HOẶC phần tử hiện tại lớn hơn phần tử cách đó 2 vị trí
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
                
        return i