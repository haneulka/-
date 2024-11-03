def solution(wallpaper):
    answer = []
    anslist=[]
    lux=luy=rdx=rdy = -1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=='#':
                if lux==-1 and luy==-1:
                    lux=rdx=i
                    luy=rdy=j
                if lux>i:
                    lux=i
                if luy>j:
                    luy=j
                if rdx<i:
                    rdx=i
                if rdy<j:
                    rdy=j
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx+1)
    answer.append(rdy+1)
    return answer