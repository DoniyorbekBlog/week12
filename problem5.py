with open("votes.txt", "r") as file:
     mydic = {}
     for line in file:
          if ":" not in line or "" in line.strip().split(':'):
               continue
          else:
               number, name = line.strip().split(':')
               if name in mydic:
                    mydic[name] += 1
               else:
                    mydic[name] = 1

          
     print(mydic)

with open("results.txt", "w") as file:
     total = sum(mydic.values())
     highest_score = 0
     winner = 0
     for name