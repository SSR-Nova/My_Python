import json

with open('server_log.txt', 'r') as file:
    lines = file.readlines()
    dict_count = {'ERROR':0, 'INFO':0}
    
    for line in lines:
        if 'ERROR' in line:
            dict_count['ERROR'] += 1
        elif 'INFO' in line:
            dict_count['INFO'] += 1

with open('stat_server_log.json', 'w') as file:
    json.dump(dict_count, file, indent=4)
    
with open('stat_server_log.json', 'r') as file:
    stat = json.load(file)
    print(stat)