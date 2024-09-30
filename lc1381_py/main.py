


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = 0
        self.msize = maxSize

    def push(self, x: int) -> None:
        if self.size < self.msize:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(self.size-1, max(-1, self.size-k-1), -1):
            self.stack[i] += val


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []  # List to hold stack elements
        self.maxSize = maxSize  # Maximum size of the stack
        self.increment_list = [0] * maxSize  # List to track increments for each level

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)  # Add element to stack

    def pop(self) -> int:
        if not self.stack:
            return -1  # Return -1 if the stack is empty

        index = len(self.stack) - 1  # Index of the top element
        # Get the value to return, add any increments it has
        value = self.stack.pop() + self.increment_list[index]

        # If there are still elements in the stack, propagate the increment to the next element
        if self.stack:
            self.increment_list[len(self.stack) - 1] += self.increment_list[index]

            # Reset increment for the removed element
        self.increment_list[index] = 0

        return value  # Return the value popped

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))  # Limit k to the current stack size
        if k > 0:
            self.increment_list[k - 1] += val

            
def main():
    print('Hello World')

if __name__ == '__main__':
    main()