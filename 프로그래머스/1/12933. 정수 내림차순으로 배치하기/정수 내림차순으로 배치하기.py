def solution(n):
    answer = 0
    tmp = 0
    ans=[]
    while n>0:
        ans.append(n%10)
        n//=10
    ans.sort(reverse=True)
    for i in ans:
        answer*=10
        answer+=i
    return answer