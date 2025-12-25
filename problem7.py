result = {}
with open("store_a.csv", "r") as store_a:
    for line in store_a:
        name, total_unit, unit_price = line.strip().split(',')
        total_unit = int(total_unit)
        unit_price = float(unit_price)
        if name in result:
            result[name][0] += total_unit
            result[name][1] += unit_price
        else:
            result[name] = [total_unit, unit_price]
with open("store_b.csv", "r") as store_b:
    for line in store_b:
        name, total_unit, unit_price = line.strip().split(',')
        total_unit = int(total_unit)
        unit_price = float(unit_price)
        if name in result:
            result[name][0] += total_unit
            result[name][1] += unit_price
        else:
            result[name] = [total_unit, unit_price]
with open("store_c.csv", "r") as store_c:
    for line in store_c:
        name, total_unit, unit_price = line.strip().split(',')
        total_unit = int(total_unit)
        unit_price = float(unit_price)
        if name in result:
            result[name][0] += total_unit
            result[name][1] += unit_price
        else:
            result[name] = [total_unit, unit_price]
with open("regional_report.txt", "w") as file:
    file.write("============================================\n")
    file.write(f"{"REGIONAL SALES CONSOLIDATION":^7}\n")
    file.write("============================================\n")
    file.write(f'Product  {"Units Sold":>17} {"Total Revenue":>40}')
    # for product, (units_solid, total) in result.items():
        # file.write(f"{product} {units_solid:<17}\n")