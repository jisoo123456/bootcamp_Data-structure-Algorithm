katok = ["다현", "정연", "쯔위", "사나", "지효"]


def delete_data(position):
    if position < 0 or position > len(katok)-1:
        print("데이터를 삭제할 범위를 벗어났습니다")
        return

    katok[position] = None

    for i in range(position, len(katok)-1):
        katok[i] = katok[i + 1]

    katok.pop()
    print(katok)


delete_data(5)