import json
def get_path(file_name):
    if file_name == "illnesses": return "data/illnesses.json"
    if file_name == "symptoms": return "data/symptoms.json"
    if file_name == "data_management": return "data_management.py"
    return None
def read(file_path):
    with open(f'{file_path}', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def name_format(name):
    parsed = str()
    for c in name:
        if c.isalpha():parsed += c
        else: parsed += ' '
    return parsed.lower()
def add_illness(name: str, symptoms: str, info: str):
    path = get_path("illnesses")
    data = read(path)
    data[name] = dict()
    data[name]["symptoms"] = symptoms
    data[name]["Info"] = info
    with open(f'{path}', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"illness added--> NAME {name} SYMPTOMS {symptoms} INFO {info}")
def add_symptoms(symptoms: list):
    path = get_path("symptoms")
    data = read(path)
    data["symptoms"] += symptoms
    with open(f'{path}', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"symptoms added --> {symptoms}")
