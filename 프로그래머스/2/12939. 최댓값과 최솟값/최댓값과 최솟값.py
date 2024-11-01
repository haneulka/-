def solution(s):
    s=s.split(' ')
    s=list(map(int,s))
    mi=str(min(s))
    ma=str(max(s))
    return mi+' '+ma