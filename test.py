import json

def file_reader(path):
    with open(path, "r", encoding="utf-8") as file:
        json_object = json.load(file)

    return json_object


def json_navigation(json_data):
    dict_print = "This is dictionary, choose a key: "
    lst_print = " This is list, choose a index: "

    while isinstance(json_data, list) or isinstance(json_data, dict):
        if isinstance(json_data,dict):
            print(json_data.keys())
            next_key = input(dict_print)
            json_data = json_data[next_key]

        if isinstance(json_data, list):
            json_len = len(json_data) - 1
            if json_len == -1:
                return f"This is your object --{json_data}--"
            next_key = input(f"Choose index between 0 and {json_len},{lst_print}")
            json_data = json_data[int(next_key)]
        

    return f"This is your object --{json_data}--"

# print(json_navigation(file_reader("frienfs_list_Obama.json")))
