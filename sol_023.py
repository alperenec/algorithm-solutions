def toplam(n):
    islem=n*(n+1)
    return islem//2
    
T = int(input())
for i in range(T):
    
    user = input().split()
    n=int(user[0])
    k=int(user[1])

    kat=toplam(k)
    if kat>n:
        print(n)
    else:
        kalan=n-kat
        ans=kalan%k
        print(ans)
    
#Distribute Chocolates sorusu.
#link: hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/distribute-chocolates-70c2c2ab/