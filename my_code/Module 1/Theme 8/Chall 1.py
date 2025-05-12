<<<<<<< HEAD
with open('notes.txt', 'r') as file:
    lines = file.readlines()
    for line_num, line in enumerate(lines, start=1):
=======
with open('notes.txt', 'r') as file:
    lines = file.readlines()
    for line_num, line in enumerate(lines, start=1):
>>>>>>> d6adf397ce76f5063ab9da53365e45c33c9cf186
        print (f'{line_num}: {line.strip()}')