import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_FILE, delimetr = ",") -> list[dict]:
    output_list = []
    with open(input_FILE) as f:

        for a, b in enumerate(f):
            if a == 0:
                headers = b[:-1].split(delimetr)
            else:
                Dict_values = dict.fromkeys(headers, 1)
                for at, bt in enumerate(Dict_values):
                    Dict_values[bt] = b[:-1].split(delimetr)[at]
                output_list.append(Dict_values)
    return (output_list)




print(json.dumps(csv_to_list_dict(INPUT_FILE), indent = 4))