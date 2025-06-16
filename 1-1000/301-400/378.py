class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a=[]
        for i in range(len(matrix)):
            for j in matrix[i]:
                a.append(j)
        return a[k-1]


# class Solution:
#     def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
#         minHeap = []
#         i = 0
#         while i < k and i < len(matrix):
#             heapq.heappush(minHeap, (matrix[i][0], i, 0))
#             i += 1
#         while k > 1:
#             k -= 1
#             _, i, j = heapq.heappop(minHeap)
#             if j + 1 < len(matrix[0]):
#                 heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))
#         return minHeap[0][0]