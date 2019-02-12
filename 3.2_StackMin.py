# 3.2 스택Min :
# 기본적인 push와 pop 기능이 구현된 스택에서 최솟값을 반환하는 min함수를 추가하려고 한다.
# 어떻게 설계할 수 있겠는가? push, pop, min연산은 모두 O(1) 시간에 동작해야 한다.

class Stack():
    def __init__(self):
        self.items = []
        self.min = None

    def push(self, item):
        if len(self.items) == 0:
            self.min = item
            self.items.append(item)
        else:
            if item < self.min:
                self.min = item
            self.items.append(item)


    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_min(self):
        return self.min


s = Stack()
s.push(3)
s.push(4)
s.push(1)
s.push(5)

print(s.get_stack())
print(s.get_min())