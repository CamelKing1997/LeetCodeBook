def findNumberIn2DArray(matrix: [[int]], target: int) -> bool:
    n = len(matrix[0])
    m = len(matrix)
    str = ""
    if target == matrix[0][0]:
        return True
    if target == matrix[0][m]:
        return True
    if target == matrix[n][0]:
        return True
    if target == matrix[n][m]:
        return True
    for i in range(n):
        for j in range(m):
            str = str + (f"{matrix[i][j]},")
        print(str)
        str = ""
    return

temp = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
num = 5
findNumberIn2DArray(temp,num)