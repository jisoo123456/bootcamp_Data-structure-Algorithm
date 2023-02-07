def is_line_full():
    global  SIZE, line, rear, front
    if rear == SIZE-1:
        return True
    return False

def is_line_empty():
    global SIZE, line, rear, front
    if front == rear:
        return True
    else:
        return False

def en_queue(data):
    global SIZE, line, rear, front
    if is_line_full():
        print("The waiting room is full!")
        return
    rear = rear + 1
    line[rear] = data

def de_queue():
    global SIZE, line, rear, front
    if is_line_empty():
        print("It's an empty line.")
        return

    front = front + 1
    out_member = line[front]
    line[front] = None

    for i in range(front+1, rear + 1):
        line[i-1] = line[i]
        line[i] = None
    front = -1
    rear = rear -1

    print(f"{out_member} enter")

SIZE = 5
line = [None for i in range(SIZE)]
rear = front = -1

en_queue("sera")
en_queue("alice")
en_queue("tom")
en_queue("tony")
en_queue("judy")
en_queue("sunny")
de_queue()
de_queue()
de_queue()
en_queue("bella")
print(f"line: {line}")