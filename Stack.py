class Stack:
    def __init__(self) -> None:
        self.__length = 0
        self.__element = None

    def is_empty(self)->bool:
        return self.__length == 0
    
    def push(self, element)->None:
        self.__element = self.__StackNode(element, self.__element)
        self.__length += 1
    
    def pop(self):
        if self.__length == 0:
            raise IndexError
        result = self.__element.value
        self.__element = self.__element.previous
        self.__length -= 1
        return result
    
    def peek(self):
        return self.__element.value
    
    def size(self)->int:
        return self.__length

    class __StackNode:
        def __init__(self, value, previous) -> None:
            self.value = value
            self.previous = previous