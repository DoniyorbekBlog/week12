with open("expenses.txt", "r") as file:
    total =0
    for line in file:
        total += float(line.strip().split(',')[1])
    print(total)