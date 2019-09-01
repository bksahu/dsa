class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binSearch(self, A, B, start, end):
        while start <= end:
            mid = (start+end)//2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1    
        return -1
    
    def search(self, A, B):
        start = 0
        end = len(A) - 1
        pivot = -1
        if A[start] < A[end]:
            pivot = 0
        else:
            while start <= end:
                mid = (start + end) // 2
                if A[mid] > A[mid + 1]:
                    pivot = mid + 1
                    break
                elif A[start] < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        
        if A[pivot] == B:
            return pivot
        elif pivot == 0:
            return self.binSearch(A, B, 1, len(A) - 1)
        elif pivot == len(A) - 1:
            return self.binSearch(A, B, 0, len(A) - 2)
        
        start = 0; end = pivot - 1
        result = self.binSearch(A, B, 0, len(A) - 2)        
                
        if result == -1:
            start = pivot + 1; end = len(A) - 1        
            result = self.binSearch(A, B, 0, len(A) - 2)  
        
        return result
