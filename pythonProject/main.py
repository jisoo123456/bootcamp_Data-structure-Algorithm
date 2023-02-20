import random
def search(array, find_data):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end)//2
        if array[mid] == find_data:
            return mid
        elif array[mid] < find_data:
            start = mid + 1
        else:
            end = mid - 1
    return -1


data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']

sell_array = [random.choice(data_array) for _ in range(20)]
sell_array.sort()
product_array = list(set(sell_array))

sell_list = []
for product in product_array:
    count = 0
    position = 0
    while position != - 1:
        position = search(sell_array, product)

        if position != - 1:
            count = count + 1
            del(sell_array[position])
    sell_list.append((product, count))

print(sell_list)
