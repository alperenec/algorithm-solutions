# https://www.hackerearth.com/problem/algorithm/inverse-graph-4c5729e8/?source=list_view
# The maximum set

import bisect

def sonuc():
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int,input().split()))
        arr.reverse()
        ans = 1
        yukle = []
        yukle.append(arr[0])
        for i in range(1,n):
            temp = bisect.bisect_left(yukle,arr[i])
            if temp == len(yukle):
                yukle.append(arr[i])
            else:
                yukle[temp] = arr[i]
        print(len(yukle))
        t -= 1

sonuc()