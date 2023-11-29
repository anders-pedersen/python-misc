# we define a list of numbers from 0 to 20
numbers = list(range(21))

# we have to create an empty list (overwrites the original list)
odd_numbers = []

# we use a for loop to iterate over the numbers in the list
for number in numbers:
    # we check the condition
    if number % 2 != 0:
        # we have to manually add the value to the list if the condition is met
        odd_numbers.append(number)
        # we end up indenting the code twice, which is not desirable as complexity grows

# let's see
print(odd_numbers)
