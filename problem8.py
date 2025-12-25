with open("grades_raw.txt", "r") as file:
    file=file.read()
    file = file.split('\n')
    try:
        for line in file:
            line = line.strip().split(',')
            if len(line) != 0:
                id, name, a1, a2, a3, exam = line
            elif len(line)==0:
                raise ValueError("  -> Error: Empty line detected")
            elif not type(a1)==type(a2)==type(a3)==type(exam)==int:
                raise ValueError('  -> Error: Invalid score format (non-numeric value)')
            elif 
    except Exception as e:
        print(e)
                