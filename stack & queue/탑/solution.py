def solution(heights):
    heights.reverse()
    answer = []
    for i in range(len(heights)):
        j = i
        flag = True
        while flag:
            try:
                if heights[i] < heights[j+1]:
                    flag = False
                    answer.append(len(heights) - j - 1)
                else: 
                    j += 1
            except:
                answer.append(0)
                flag = False

    answer.reverse()
    return answer