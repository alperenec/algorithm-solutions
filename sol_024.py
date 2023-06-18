def yuksekDeg():
    t = int(input())

    while t:
        c = 1
        n = int(input())
        top = 0

        while c*2-1 <= n:
            c = c*2
            top = c-1

        print(top)
        t = t-1

yuksekDeg()

#Set Numbers sorusu.
#link: hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/set-numbers-bea74f5a/