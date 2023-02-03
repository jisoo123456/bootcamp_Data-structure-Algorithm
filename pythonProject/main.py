#시간이 부족해서 다 못했습니다. 시간이 마무리 되서 일단 오늘 안에 완성해서 제 깃에 업로드하겠습니다
def find_and_insert_data(pokemon, health):
	find_pos = -1
	for i in range(len(pokemons)) : #(0~3)
		pair = pokemons.values(i)
		if health >= pair :  #i = 2
			find_pos = i     #find_pos = 2
			break
	if find_pos == -1:
		findPos = len(pokemons)

	insert_data(find_pos, (pokemon, health))


def insert_data(position, **pokemon):
	if position < 0 or position > len(pokemon):
		print("데이터를 삽입할 범위를 벗어났습니다.")
		return

	pokemons.append(None)

	for i in range(len(pokemons) - 1, position, -1):
		pokemons[i] = pokemons[i - 1]

	pokemons[position] = pokemon


pokemons = {"피카츄" : 100, "파이리" : 80, "꼬부기" : 30, "라이츄" : 10}  #이상해 50[피카츄 파이리 이상해 꼬부기 라이츄]


if __name__ == "__main__":

	while True:
		pokemon = input("추가할 포켓몬--> ")
		health = int(input(f"{pokemon}의 능력치--> "))
		find_and_insert_data(pokemon, health)
		print(pokemons)
