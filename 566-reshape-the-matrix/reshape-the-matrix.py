class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        ans = [[0] * c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                x = i * n + j
                ans[x // c][x % c] = mat[i][j]

        return ans