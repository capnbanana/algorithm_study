# p.147 [스택과 큐]
# 3.1 한 개로 세개 : 배열 한개로 스택 세 개를 어떻게 구현할지 설명하라.


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
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

class ThreeInOne():
    def __init__(self, arr, num1, num2, num3):
        self.arr = arr
        self.num1, self.num2, self.num3 = num1, num2, num3
        self.stack1, self.stack2, self.stack3 = Stack(), Stack(), Stack()

    def divideIntoThree(self):

        for i in range(self.num1):
            self.stack1.push(arr[i])

        for j in range(self.num1, self.num1 + self.num2):
            self.stack2.push(arr[j])

        for k in range(self.num1 + self.num2, self.num1 + self.num2 + self.num3):
            self.stack3.push(arr[k])

        # print(self.stack1.get_stack(), self.stack2.get_stack(), self.stack3.get_stack())

        return self.stack1, self.stack2, self.stack3




arr = list(range(1,21))

s = ThreeInOne(arr, 3, 4, 13)

stack1, stack2, stack3 = s.divideIntoThree()

print(stack1.get_stack())
print(stack2.get_stack())
print(stack3.get_stack())

