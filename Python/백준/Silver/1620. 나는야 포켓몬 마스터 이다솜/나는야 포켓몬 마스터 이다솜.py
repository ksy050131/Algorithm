pokemonNum, testCase = map(int, input().split())

pokemon = {}
reverse_pokemon = {}

for i in range(1, pokemonNum + 1):
    name = input()
    pokemon[i] = name         # 번호 -> 이름
    reverse_pokemon[name] = i # 이름 -> 번호

for _ in range(testCase):
    command = input()
    if command.isdigit():
        print(pokemon[int(command)])
    else:
        print(reverse_pokemon[command])
