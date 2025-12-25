with open("raw_users.txt", "r") as file, open("clean_profiles.txt", 'w') as file2:
    for line in file:
        line = line.strip().split('-')
        full_name = line[0].strip().split()
        name1 = full_name[0][0].upper() + full_name[0][1::].lower()
        name2 = full_name[1][0].upper() + full_name[1][1::].lower()
        age = 2025-int(line[1].strip())
        file2.write(f'Name: {name1} {name2} (Age: {age})\n')