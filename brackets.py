from Stack import Stack

def check_brackets(brackets:str):
    if len(brackets) %2 == 1:
        return False
    open_brackets = '({['
    close_brackets = ')}]'
    stack = Stack()
    for bracket in brackets:
        if bracket in open_brackets:
            for n, el in enumerate(open_brackets):
                if bracket == el:
                    stack.push(n)
                    break
        else:
            if bracket != close_brackets[stack.pop()]:
                return False
    return True