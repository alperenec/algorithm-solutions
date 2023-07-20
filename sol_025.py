# https://www.hackerearth.com/problem/algorithm/hill-150045b2/?source=list_view
# Length of a valley

def answer():
    t = int(input())
    while(t):
        n = int(input())
        arr = list(map(int,input().split()))
        sol = [0]*n
        sag = [0]*n
        sol[0] = 1
        c = 1
        for i in range(1,n):
            if(arr[i]<arr[i-1]):
                c+=1
            else:
                c = 1
            sol[i] = c
        c = 1
        sag[n-1] = 1
        for i in range(n-2,-1,-1):
            if(arr[i]<arr[i+1]):
                c+=1
            else:
                c = 1
            sag[i] = c
        for i in range(n):
            print(sag[i]+sol[i]-1,end=" ")
        print()
        t-=1
answer()