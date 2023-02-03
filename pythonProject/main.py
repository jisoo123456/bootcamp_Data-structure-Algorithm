katok = ['다현', '정연', '쯔위', '사나', '지효']

def insert_data(position, friend):
	if position < 0 or position > len(katok):
		print("데이터를 삽입할 범위를 벗어났습니다")
		return #이 함수를 빠져 나가기 위해서 return 작성

	katok.append(None)

	for i in range(len(katok)-1, position, -1):
		katok[i] = katok[i-1]

	katok[position] = friend
	print(katok)

insert_data(2, "나연")
