# https://www.hackerearth.com/problem/algorithm/strange-matrix-8b96f2ab/?source=list_view 
# A strange matrix

import heapq
 
def control(x, y, n, m):
    return x < n and x >= 0 and y < m and y >= 0
 
def minTime(ans, n, m, c):
    ara = [[float('inf') for i in range(m)] for i in range(n)]
    ara[0][0] = 0
    arr = []
    heapq.heappush(arr, (0, 0, 0))
    while arr:
        tempTime, x, y = heapq.heappop(arr)
        if x == n - 1 and y == m - 1:
            return tempTime
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if control(i, j, n, m):
                temp = min(ans[x][y] + tempTime, c)
                target = min(ans[i][j] + tempTime, c)
                nextTime = tempTime
                if temp != target:
                    nextTime += max(abs(c - temp), abs(c - target))
                if nextTime < ara[i][j]:
                    ara[i][j] = nextTime
                    heapq.heappush(arr, (nextTime, i, j))
    return -1
 
if __name__ == '__main__':
    n, m, c = map(int, input().split())
    ans = [[int(x) for x in input().split()] for i in range(n)]
    print(minTime(ans, n, m, c))