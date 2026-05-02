class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        mid=0
        while left<=right:
            mid=left+(right-left)//2
            row=mid//n
            col=mid%n
            element=matrix[row][col]
            if element==target:
                return True
            elif element<target :
                left=mid+1
            else:
                right=mid-1
        return False       


