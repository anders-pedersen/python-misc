names_1 = ["Michele", "Robin", "Sara"]
names_2 = ["Michele", "Robbyn", "Sarah"]
names_3 = ["Michelelele", "Robin", "Sarah"]
names = names_1 + names_2 + names_3

# Create your dictionary here
names_dict = {name: names.count(name) for name in names}

print(names_dict)
