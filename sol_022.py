user = input().split()
n=int(user[0])
k=int(user[1])

def sayici(n, k):
    tas= [0]*(n+1)
    tas[1] = 1

    for i in range(2, n+1):
        for j in range(1, min(k, i)+1):
            tas[i] = (tas[i] + tas[i-j]) % (10**9+7)
    return tas[n]

print(sayici(n, k))

#Jumping Stones sorusu.
#Link: hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/jump-k-forward-250d464b/