# 1 번문제  P511 
# range(0, rowCount + 1) , weight[row] > col 사용

def knapsack():
    # 0으로된 2차배열 리스트를 생성한다.
    array = [[0 for _ in range(maxWeight + 1)]for _ in range(rowCount + 1)]
    for row in range(1, rowCount + 1):  # 1개에서 rowCount + 1까지
        for col in range(1, maxWeight + 1): # 무게가 1에서 maxWeight+1까지
            if weight[row] > col:   # 무게가 열보다 크면
                array[row][col] = array[row - 1][col]   # 위에있는 가격을 넣는다
            else:   # 그외 무게가 작거나같으면
                value1 = money[row] + array[row - 1][col - weight[row]] #  
                value2 = array[row - 1][col]
                array[row][col] = max(value1, value2)

    return array[rowCount][maxWeight]