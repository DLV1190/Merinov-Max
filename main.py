f = open("game.csv", encoding="utf-8").readlines()
f.pop(0)
a = open("game_new.txt", "w", encoding="utf-8")
for i in f:
    ent = i.split(",")
    if ent[1] == "Avery":
        a.write(f"У персонажа {ent[1]} в игре {ent[0]} нашлась ошибка с кодом: {ent[2]}. Дата фиксации: {ent[3]}")
