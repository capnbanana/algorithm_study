# 2.3 중간 노드 삭제 :
# 단반향 연결리스트가 주어졌을 때 중간(정확히 가운데 노드일 필요는 없고 처음과 끝 노드만 아니면 된다)에 있는 노드 하나를 삭제하는 알고리즘을 구현하라.
# 단, 삭제할 노드에만 접근 할 수 있다.
# 예제) 입력 : 연결리스트 a -> b -> c -> d -> e에서 노드 c
# 결과 : 아무것도 반환할 필요는 없지만, 결과로 연결리스트 a -> b -> d -> e가 되어 있어야한다.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init_list(lst):
    nodelist = []
    for i in lst:
        node = Node(i)
        nodelist.append(node)
    for j in range(len(nodelist)):
        if j+1 < len(nodelist):
            nodelist[j].next = nodelist[j+1]

    return nodelist

def deleteMiddleNode(lst):
    nodelist = init_list(lst)
    MiddleNum = len(lst) / 2
    MiddleNum = int(MiddleNum)
    nodelist[MiddleNum-1].next = nodelist[MiddleNum+1]
    return nodelist

def printResult(lst):
    finalList = deleteMiddleNode(lst)
    node = finalList[0]
    while node:
        print(node.data)
        node = node.next

lst = ['a','b','c','d','e']
lst2 =  [1,2,3,4,5,6,7]


printResult(lst)
printResult(lst2)


# def init_list():
#     global node1, node2, node3, node4, node5
#     node1 = Node('a')
#     node2 = Node('b')
#     node3 = Node('c')
#     node4 = Node('d')
#     node5 = Node('e')
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#
# def Main():
#     init_list()
#     node = node1
#     while node:
#         print (node.data)
#         node = node.next
#
# def deleteMiddleNode():
#     Main()
#
# Main()