f = open("game.csv", encoding="utf-8").readlines()
f.pop(0)
f2 = open("problem_2_answer.txt", "w", encoding="utf-8")
a = []
for i in f:
    a.append(i.split(","))
list_char = ['Aaliyah', 'Aaron', 'Abigail', 'Adeline', 'Aiden', 'Alex', 'Alexander', 'Amelia', 'Andrew', 'Aria', 'Aubrey', 'Ava', 'Avery', 'Benjamin', 'Brooklyn', 'Caleb', 'Camila', 'Charles', 'Charlie', 'Charlotte', 'Chloe', 'Daniel', 'David', 'Eleanor', 'Elijah', 'Elizabeth', 'Ella', 'Ellie', 'Emily', 'Emma', 'Ethan', 'Eva', 'Evelyn', 'Gabriel', 'Gia', 'Grace', 'Hannah', 'Harper', 'Hazel', 'Henry', 'Isaac', 'Isabella', 'Jack', 'Jackson', 'Jacob', 'James', 'Jayden', 'John', 'Joseph', 'Julia', 'Julian', 'Layla', 'Leah', 'Leo', 'Levi', 'Liam', 'Lily', 'Logan', 'Lucas', 'Lucy', 'Luna', 'Madelyn', 'Madison', 'Mason', 'Matthew', 'Mia', 'Michael', 'Mila', 'Natalie', 'Nathan', 'Noah', 'Nora', 'Oliver', 'Olivia', 'Owen', 'Penelope', 'Peyton', 'Riley', 'Ruby', 'Sadie', 'Samantha', 'Samuel', 'Scarlett', 'Sofia', 'Sophia', 'Sophie', 'Stella', 'Victoria', 'William', 'Zoe', 'Zoey']
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if list_char.index(a[i][1]) > list_char.index(a[j][1]):
            a[i], a[j] = a[j], a[i]
count = 0
list_char_new = []
for i in a:
    count = 0
    if i[1] not in list_char_new:
        for j in a:
            if j[1] == i[1]:
                count += 1
        f2.write(f'{i[1]} - количество багов: {count}\n')
        list_char_new.append(i[1])
