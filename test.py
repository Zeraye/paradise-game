import json
with open("levels.json", "r+") as read_file:
    data = json.load(read_file)
    levels_easy = (data['levels_easy'])
    levels_med = (data['levels_med'])
    levels_hard = (data['levels_hard'])
print(levels_easy)
def write_json(data, filename='levels.json'):
    with open(filename, 'r+') as f:
        json.dump(data, f)

levels_easy[0] = True
with open('levels.json', 'r+') as file:
    data = json.load(file)
    new_data = {'levels_easy': levels_easy}
    data.update(new_data)
    write_json(data)
