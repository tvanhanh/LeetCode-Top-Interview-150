class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n # Xử lý trường hợp k lớn hơn độ dài mảng
        
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Bước 1: Đảo toàn bộ
        reverse(0, n - 1)
        # Bước 2: Đảo k thằng đầu
        reverse(0, k - 1)
        # Bước 3: Đảo phần còn lại
        reverse(k, n - 1)