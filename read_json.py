import json


try:
    path = input()
    file = open(path, "rt", encoding="utf-8")
    json_data = file.read()
    data = json.loads(json_data)
    print(data)
    file.close()
except(FileNotFoundError):
    print("Ocorreu um erro!")
finally:
    print("Processo concluído")
    