col, row = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
    
for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '.':
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if not(x < 0 or y < 0 or x >= row or y >= col):
                        if matrix[x][y] == '*':
                            count += 1
            matrix[i][j] = count
            print(matrix[i][j], end ='')
        else:
            print(matrix[i][j], end='')
    print()