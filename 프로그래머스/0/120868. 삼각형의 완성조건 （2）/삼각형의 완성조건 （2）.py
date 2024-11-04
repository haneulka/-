def solution(sides):
    answer=0
    for i in range(1, sides[0]+sides[1]):
        ma=max(max(sides),i)
        if ma<i+sides[0]+sides[1]-ma:
            answer+=1
    return answer