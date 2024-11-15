def solution(s):
    answer = True
    pcount=0
    ycount=0
    for i in s:
        if i=='p'or i=='P':
            pcount+=1
        elif i=='y'or i=='Y':
            ycount+=1
    if ycount!=pcount:
        answer=False
    return answer