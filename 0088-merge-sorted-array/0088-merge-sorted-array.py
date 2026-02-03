class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # p1: con trỏ trỏ vào số cuối cùng thực sự của nums1
        p1 = m - 1
        # p2: con trỏ trỏ vào số cuối cùng của nums2
        p2 = n - 1
        # p: con trỏ trỏ vào vị trí cuối cùng tuyệt đối của mảng nums1 (vị trí để điền số)
        p = m + n - 1
        
        # Duyệt khi cả hai mảng đều còn số
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                # Nếu số ở nums1 lớn hơn, đặt nó vào vị trí p
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Nếu số ở nums2 lớn hơn hoặc bằng, đặt nó vào vị trí p
                nums1[p] = nums2[p2]
                p2 -= 1
            # Sau mỗi lần đặt, lùi vị trí điền số về phía trước
            p -= 1
            
        # Nếu nums2 vẫn còn số (trường hợp nums1 hết trước)
        # thì chép nốt phần còn lại của nums2 vào đầu nums1
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]