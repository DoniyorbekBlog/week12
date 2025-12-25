errors = 0
with open('server_log.txt', "r") as file, open("urgent_alerts.txt", "a") as urgent_file:
    for line in file:
        if "ERROR" in line:
            urgent_file.write(line)
            errors += 1
    print(errors)