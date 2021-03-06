# 题目：
# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:continue
                elif i==0:grid[i][j]=grid[i][j]+grid[i][j-1]
                elif j==0:grid[i][j]=grid[i][j]+grid[i-1][j]
                else: grid[i][j]=grid[i][j]+max(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

if __name__ == '__main__':
    print(Solution().maxValue([[1,3,1],[1,5,1],[4,2,1]]))

