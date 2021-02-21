def cavityMap(grid):
    grid1=grid.copy()
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            if(grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1]):
                grid1[i][j]="X"
    for i in grid1:
        print(''.join(i))
n = int(input())
grid = []
for _ in range(n):
    grid_item = list(input())
    grid.append(grid_item)
result = cavityMap(grid)

