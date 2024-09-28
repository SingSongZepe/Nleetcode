

class MyCircularDeque:

    def __init__(self, k: int):
        self.cap: int = k
        self.data = [-1] * k
        self.size: int = 0
        if k > 1:
            self.head: int = 0
            self.tail: int = 1
        else:
            self.head: int = 0
            self.tail: int = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.head] = value
        self.head = (self.head - 1) % self.cap
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.cap
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.cap
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.head + 1) % self.cap]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.tail - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
def main():
    print('Hello World')

if __name__ == '__main__':
    main()