dic = {}
over_500 = []
def process_donations(donations):
    with open("donations.txt", "r") as file:
        for line in file:
            line=line.strip().split(',')
            try:
                donor_name = line[0]
                cause = line[1]
                check = float(line[2])
                cash = float(line[3])
                total = cash + check
                if cause in dic:
                    dic[cause]+=total
                else:
                    dic[cause]=total
                if total>500:
                    over_500.append([donor_name, total])
            except ValueError:
                continue
    return dic, over_500
    
def write_fundraising_report(cause_totals, top_donors):
    with open("fundraising_summary.txt", "w") as file:
        file.write("FUNDS RAISED PER CAUSE\n----------------------\n")
        for cause, total in dic.items():
            file.write(f"{cause}: ${total:.2f}\n")
        file.write("\nGOLD TIER DONORS (> $500)\n----------------------\n")
        if not len(over_500):
            file.write("There is no Gold Tier Donors")
        else:
            for name, total in over_500:
                    file.write(f"{name} (${total})\n")
cause_totals, top_donars = process_donations("donations.txt")
write_fundraising_report(cause_totals, top_donars)
