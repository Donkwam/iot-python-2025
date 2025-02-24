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
sellAry = [random.choice(dataAry) for _ in range(20)]

print('오늘 판매된 물건(중복O) --> ', sellAry)

# 메인코드
node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            break
        if name < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            current = current.right
print('이진 탐색 트리 구성 완료!')

def preorder(node):
    if node == None:
        return
    print(node.data,end=' ')
    preorder(node.left)
    preorder(node.right)

print('오늘 판매된 종류(중복X) --> ', end=' ')
preorder(root)
