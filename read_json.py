import json


try:
    path = input()
    file = open(path, "rt", encoding="utf-8")
    data = json.load(file)
    print(data)
    file.close()
except(FileNotFoundError):
    print("Ocorreu um erro!")
finally:
    print("Processo concluído")
    