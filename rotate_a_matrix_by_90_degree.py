# 2차원 리스트를 90도 회전한 결과를 반환하는 함수

def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for i in range(m)]    # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
            
    return result

def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for i in range(m)]    # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
            
    return result
   
def rotate_90_left(graph): # 4
    new_graph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_graph[i][j] = graph[j][m-1-i]
    return new_graph