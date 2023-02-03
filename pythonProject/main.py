katok = ["다현", "정연", "쯔위", "사나", "지효", "나연"]


def delete_data(position):
    if position < 0 or position > len(katok)-1:
        print("데이터를 삭제할 범위를 벗어났습니다")
        return

    for i in range(position, len(katok)):
        katok.pop()

    print(katok)


delete_data(1)