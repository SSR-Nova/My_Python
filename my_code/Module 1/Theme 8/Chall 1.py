with open('notes.txt', 'r') as file:
    lines = file.readlines()
    for line_num, line in enumerate(lines, start=1):
        print (f'{line_num}: {line.strip()}')