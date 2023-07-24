# 알고리즘 복잡도
# 점근적 복잡도

def matrix_mult(mat_a, mat_b, mat_result, n):
    for i in range(n):
        for j in range(n):
            mat_result[i][j] = 0
            for k in range(n):
                mat_result[i][j] = mat_result[i][j] + mat_a[i][k] * mat_b[k][j]

# Θ(n³)
