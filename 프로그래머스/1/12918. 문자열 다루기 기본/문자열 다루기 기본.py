def solution(s):
    answer = True
    s=list(s)
    for i in s:
        if (ord(i)>57):
            answer=False
            print(i, ord(i))
    if not(len(s)==4 or len(s)==6):
        answer=False
    return answer