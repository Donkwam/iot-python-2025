# P269 2번

def isQueueFull():
    global SIZE, queue, front, rear #  SIZE, queue, front, rear를 global함수로 가져온다.
    if (rear == SIZE -1):   # rear가 SIZE-1일때 True 그외 False
        return True
    else:
        return False
        
def isQueueEmpty(): # 두개같 같으면 True 그외 False
    global SIZE, queue, front, rear
    if(front == rear):  
        return True
    else:
        return False
        
def enQueue(data):  # 손님을 차례대로 리스트안에 넣어준다 
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐가 꽉 찼습니다.')
        return
    rear = rear+1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    front += 1
    data = queue[front] # enQueue한 사람의 리스트에 None을 넣는다
    queue[front] = None

    for i in range(front+1, rear+1):  # 빠진자리를 채우기위해 뒤에 사람들을 앞으로 한칸씩간다.  
        queue[i-1]= queue[i]
        queue[i] = None
    front = -1
    rear -= 1

    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):    #
        print('큐가 비었습니다.')
        return None
    return queue[front+1]

SIZE = int(input('큐크기 입력 > '))
queue = [None for _ in range(SIZE)] # SIZE 갯수만큼 None 리스트를 생성하겠다.
front = rear = -1 

if __name__ == '__main__': # 메인 실행함수
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q)').upper()   # 영어 대문자로 입력받음
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')  # 입력 받아서 data에 넣음
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select == 'E': # 앞에서 부터 빠진다
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select == 'V': 
            data = peek()   # 데이터 나열한다.
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        else:
            print('입력 오류')

        