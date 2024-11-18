def solution(s):
    answer = True
    op=0
    cl=0
    for i in s:
        if i=='(':
            op+=1
        if i==')':
            cl+=1
            if op<cl:
                answer=False
                break;
    if op!=cl:
        answer=False
    return answer