## Сложность алгоритма O((n+1)*(m+1))
def uniquePathsWithObstacles(obstacleGrid):  
    m, n = len(obstacleGrid), len(obstacleGrid[0])        
    dp=[[0] * (n+1) for _ in range(m+1)]     ##Создаём матрицу   
    dp[0][1]=1       
    for row in range(1, m+1):   ## Проходимся по ней
        for col in range(1, n+1):
            if not obstacleGrid[row-1][col-1]:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[-1][-1] ##Возвращаемся самый крайний элемент, он и будет искомым