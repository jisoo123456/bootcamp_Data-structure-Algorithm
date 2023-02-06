import random

def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    else:
        return False

def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if is_stack_full():
        return
    else:
        top = top + 1
        stack[top] = data

def pop():
    global SIZE, stack, top

    if is_stack_empty():
        return
    else:
        data = stack[top]
        stack[top] = None
        top = top - 1
        return data

SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1

if __name__=="__main__":
    stone_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    random.shuffle(stone_color)

    print("go snack house:", end = ' ')
    for stone in stone_color:
        push(stone)
        print(stone, '->', end = ' ')
    print("snack house")

    print("go home:", end = ' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, '->', end = ' ')
    print("home")