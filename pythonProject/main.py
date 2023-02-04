def find_and_insert_data(pokemon, health):
	find_pos = -1
	list_pokemons_keys = list(pokemons.keys())
	list_pokemons_value = list(pokemons.values())

	for i in range(len(list_pokemons_value)):
		pair = list_pokemons_value[i]
		if health >= pair:
			find_pos = i
			break
	if find_pos == -1:
		find_pos = len(pokemons)

	insert_data(find_pos, pokemon, health)

def insert_data(position, pokemon, health):
	if position < 0 or position > len(pokemons):
		print("데이터를 삽입할 범위를 벗어났습니다.")
		return

	append_pokemons = {pokemon : health}
	first_pokemons = {}
	last_pokemons = {}

	list_pokemons_keys = list(pokemons.keys())
	list_pokemons_values = list(pokemons.values())

	for i in range(position):
		first_pokemons.update(list_pokemons_keys[i])
	for k in range(position, len(pokemons)):
		last_pokemons.update(list_pokemons_keys[k])

	new_pokemons = {}
	if position == 0:
		new_pokemons.update(append_pokemons)
		new_pokemons.update(first_pokemons)
		new_pokemons.update(last_pokemons)

	else:
		new_pokemons.update(first_pokemons)
		new_pokemons.update(append_pokemons)
		new_pokemons.update(last_pokemons)

	print(new_pokemons)

pokemons = {"피카츄" : 100, "파이리" : 80, "꼬부기" : 30, "라이츄" : 10}

if __name__=="__main__":

	while True:
		pokemon = input("추가할 포켓몬:")
		health = int(input(f'{pokemon}의 능력치:'))
		find_and_insert_data(pokemon, health)