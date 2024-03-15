f = open("game.csv", encoding="utf-8").readlines()
f.pop(0)
a = []
for i in f:
    a.append(i.split(","))
f2 = open("problem_3_answer.txt", "w", encoding="utf-8")
error = str(input())
while error != "game":
    count = 0
    for i in a:
        if i[2] == error:
            f2.write(f'Ошибка {error} встречается в игре {i[0]} у персонажа {i[1]}.\n')
            count += 1
    if count == 0:
        f2.write("Этой ошибки не существует\n")
    f2.write("\n")
    error = input()
