with open("story.txt", "r") as file, open("stopwords.txt", 'r') as stopping:
    text = file.read().replace('\n', '').lower().replace(".", "").replace(",", "").replace("?", "")
    text = text.split()
    stopwords = stopping.read().split()
    mydic = {}
    for word in text:
        
        if word not in stopwords:
            if word in mydic:
                mydic[word] += 1
            else:
                mydic[word] = 1

with open("analysis.txt", "w") as file:
    file.write("WORD FREQUENCY REPORT\n")
    file.write("---------------------\n")
    for word, number in mydic.items():
        file.write(f'{word}: {number}\n')


        
        
