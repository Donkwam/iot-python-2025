# 3번 P309

import random
# 함수 선언
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
        
# 전역변수
memory = []
root = None
dataAry =[ '콘말차', '삿포로 맥주', '아카페라 벤티 헤이즐넛', '레어치즈푸딩', '척오리지널 메가 사워', '요아정 요거트컵', 
          '페퍼로니피자주먹밥', '널담 슈톨렌', '딸기마시멜로케이크', '버니공쥬 딸기뚱카롱', '고추잡채호빵', '체다 슈크림붕어스낵' ]
sellAry = []

print("밑에 메뉴를 보고 상품을 입력하세요. ")
print(f'상품종류 {dataAry}')
while True:
    select = input('삽입(I)/종료(Q)').upper()   # i입력시 menu에 값이 입력해야 되고 q를 눌리면 코드가 끝난다. 
    if select == 'I':
        menu = input("상품명: ")
    if select == 'Q':
        break
    sellAry.append(menu)

sellAry = [random.choice(sellAry) for _ in range(5)] # 20개를 메뉴중에 아무거나 뽑는다.

print('오늘 판매된 물건(중복O) --> ', sellAry)

# 메인코드
node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[0:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:    # 판매되었으면 넘어감
            break
        if name < current.data:   # 비교할 값이 크면 실행
            if current.left == None:
                current.left = node
                memory.append(node) # 판매되지 않은 것들을 메모리에 추가
                break
            current = current.left
        else:   # 비교할 값이 작거나 그외 실행
            if current.right == None:
                current.right = node
                memory.append(node) # 판매되지 않은 것들을 메모리에 추가
                break
            current = current.right
print('이진 탐색 트리 구성 완료!')

def preorder(node): # 중복이 인제 아닌지 확인후 
    if node == None:
        return
    print(node.data,end=' ')
    preorder(node.left)
    preorder(node.right)

print('오늘 판매된 종류(중복X) --> ', end=' ')
preorder(root)
