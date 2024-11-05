def solution(spell, dic):
    answer = 2
    for i in range(len(dic)):
        count=0
        for j in range(len(spell)):
            for k in range(len(dic[i])):
                if (dic[i][k]==spell[j]):
                    count+=1
                    break;
        if (count==len(spell)):
            print(dic[i])
            answer=1
    return answer