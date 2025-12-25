with open("inventory.csv", "r") as file, open("reqorder_list.txt", "w") as file2:
    for line in file:
        line = line.strip().split(',')
        stock, req = line[1:3]
        stock=int(stock)
        req=int(req)
        if stock < req:
            file2.write(str(req-stock)+'\n')
