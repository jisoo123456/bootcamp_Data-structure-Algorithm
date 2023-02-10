def solution(s, skip, index):
    a = list(s)
    list1 = []
    for i in a:
        string1 = (chr(ord(i)+index))
        if string1 in skip:
            for j in range(1,):
                string1  = (chr(ord(i)+index+j))
                return string1
        list1.append(string1)

    answer = ''.join(list1)
    print(answer)

s = input("input string(5~50):")
skip = input("input skip(1~10):")
index = int(input("input index(1~20):"))

solution(s, skip, index)