n = int(input("Enter the number: "))
l = []  # Initialize the list outside the loop

for i in range(1, 11):
    l.append(f"{n} x {i} = {n * i}")  # Append the formatted string to the list

a = "\n".join(l)

print(a)

