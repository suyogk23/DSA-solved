class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time: O(log (m) + log (n)) = O(log(m*n))
        n = len(matrix) # rows
        m = len(matrix[0]) # cols

        def searchRow(row, l, r): #O(log m)
            while l <= r:
                mid = (l+r)//2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return False # element not found

        lr, rr = 0, n-1
        while lr <= rr: # O(log n)
            mr = (lr + rr)//2
            if matrix[mr][0] <= target and target <= matrix[mr][m-1]:
                # print(mr)
                return searchRow(mr, 0, m-1)
            if matrix[mr][0] > target:
                rr = mr-1
            else:
                lr = mr+1
        
        return False
