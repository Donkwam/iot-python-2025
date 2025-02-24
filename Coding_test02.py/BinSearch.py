# 4번
count = 0
def binSearch(ary, fData):
    global count
    pos = -1
    start = 0
    end = len(ary) -1
    

    while (start <= end):   # 시작이 끝보다 커지면 실패
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1 # 뒤쪽에 데이터가 있다
            count += 1
        else:
            end = mid - 1   # 앞쪽에 데이터가 있다
            count += 1
        
    return pos


dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 160

print(f'배열 --> {dataAry}')    # dataAry리스트 출력
pos = binSearch(dataAry, findData)  
if pos == -1:   # pos가 -1이면 밑에 출력
    print(f'{findData}(이)가 없음')
else:   # 그외 이것 출력
    print(f' {findData} / {pos}에 위치해 있음')
    print(f'검색횟수 {count}')
