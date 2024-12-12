def solution(n, m):
    answer = []
    big=0
    if n>m:
        tmp=n
        n=m
        m=tmp
    for i in range(n):
        if (n%(i+1)==0 and m%(i+1)==0):
            if (big<(i+1)):
                big=i+1
    answer.append(big)
    answer.append(n*m/big)
    return answer