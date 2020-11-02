def rotate(matrix: [[int]]) -> None:
    def next_xy(x, y, s):
        return y, s - 1 - x
    n = len(matrix)
    i = 0
    for i in range(n):
        l = n - i * 2
        if l < 2:
            break
        for j in range(l - 1):
            x, y = 0, j
            t = matrix[x + i][y + i]
            for k in range(4):#
                nx, ny = next_xy(x, y, l)
                print(x, y, nx, ny)
                print(t, matrix[nx + i][ny + i])
                tt = matrix[nx + i][ny + i]
                matrix[nx + i][ny + i] = t
                x, y, t = nx, ny, tt
    print(matrix)

rotate([[1,2,3],[4,5,6],[7,8,9]])