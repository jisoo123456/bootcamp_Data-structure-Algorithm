def add_data(friend):
	katok.append(friend)

def insert_data(position, friend):
	if position < 0 or position > len(katok):
		print("데이터를 삽입할 범위를 벗어났습니다")
		return #이 함수를 빠져 나가기 위해서 return 작성

	katok.append(None)

	for i in range(len(katok)-1, position, -1):
		katok[i] = katok[i-1]

	katok[position] = friend

def delete_data(position):
	if position < 0 or position > len(katok)-1:
		print("데이터를 삭제할 범위를 벗어났습니다")
		return
	for i in range(positon, len(katok)-1):
		katok[i] = katok[i+1]

	katok.pop()
	print(katok)


if __name__ == "main":

	while (select !=4):

		select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"))

		if(select == 1):
			data = input("추가할 데이터-->")
			add_data(data)
			print(katok)

		elif(select == 2):
			pos = int(input("삽입할 위치-->"))
			data = int(input("추가할 데이터"))
			insert_data(pos, data)
			print(katok)

		elif(select == 3):
			pos = int(input("삭제할 위치-->"))
			delete_data(pos, data)
			print(katok)

		elif(select == 4):
			print(katok)
			exit()
		else:
			print("1~4 중 고르세요!")
			continue