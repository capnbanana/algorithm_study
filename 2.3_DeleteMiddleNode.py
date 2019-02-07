# 2.3 중간 노드 삭제 :
# 단반향 연결리스트가 주어졌을 때 중간(정확히 가운데 노드일 필요는 없고 처음과 끝 노드만 아니면 된다)에 있는 노드 하나를 삭제하는 알고리즘을 구현하라.
# 단, 삭제할 노드에만 접근 할 수 있다.
# 예제) 입력 : 연결리스트 a -> b -> c -> d -> e에서 노드 c
# 결과 : 아무것도 반환할 필요는 없지만, 결과로 연결리스트 a -> b -> d -> e가 되어 있어야한다.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node1, node2, node3, node4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3.33333)
    node4 = Node('four')
    node1.next = node2
    node2.next = node3
    node3.next = node4

def Main():
    init_list()
    node = node1
    while node:
        print (node.data)
        node = node.next

Main()