names_1 = ["Michele", "Robin", "Sara"]
names_2 = ["Michele", "Robbyn", "Sarah"]
names_3 = ["Michelelele", "Robin", "Sarah"]
names = names_1 + names_2 + names_3

# Create your dictionary here
names_dict = {}

for name in names:
    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

print(names_dict)
