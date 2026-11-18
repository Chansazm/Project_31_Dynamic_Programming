def gridtravelertab(m,n):
    if m == 0 or n == 0: return 0
    Table = [[0] * (n+1) for row in range(m+1)]
    Table[1][1] = 1
    
    for i in range(m+1):
        for j in range(n+1):
            current = Table[i][j]
            if j+ 1 <= n:
                Table[i][j+1] += current
            if i + 1 <= m: 
                Table[i+1][j] += current
    return Table[m][n]







#Driver function
#Time Complexity:: memoised is n * m unmemoised is 2^(n+m)
#Space Complexity:: n
print(gridtravelertab(2,3)) # 3
#print(gridtravelertab(1000,1000))# 2333606220