

import pylightxl as xl
import json

def classify(code:str, name:str) -> bool:
    data_saved = True
    category = int(input(f'{name} '))

    data = {code: name}

    if category == 1:
        update_json(str(category), data)
    elif category ==2:
        update_json(str(category), data)
    elif category ==3:
        update_json(str(category), data)
    elif category ==4:
        update_json(str(category), data)
    elif category ==5:
        update_json(str(category), data)
    elif category ==6:
        update_json(str(category), data)
    elif category ==7:
        update_json(str(category), data)
    elif category ==8:
        update_json(str(category), data)
    elif category ==9:
        update_json(str(category), data)
    elif category ==10:
        update_json(str(category), data)
    elif category ==11:
        update_json(str(category), data)
    elif category ==12:
        update_json(str(category), data)
    elif category ==13:
        update_json(str(category), data)
    elif category ==14:
        update_json(str(category), data)
    elif category ==15:
        update_json(str(category), data)
    elif category ==16:
        update_json(str(category), data)
    else:
        print('Buen intento crack')
        data_saved = False

    if data_saved:
        print('Fila guardada correctamente')
    return data_saved


def update_json(category: str, data: dict) -> None:
    with open('data.json') as json_file:
        json_data = json.load(json_file)

    json_data[category].append(data)

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

def main() -> None:
    # readxl returns a pylightxl database that holds all worksheets and its data
    db = xl.readxl(fn='PA.xlsx')

    # return all sheetnames
    codes = db.ws(ws='Hoja1').col(col=1)
    names = db.ws(ws='Hoja1').col(col=2)

    for code, name in zip(codes, names):
        write_success = False
        while not write_success:
            write_success = classify(code, name)


if __name__ == "__main__":
    main()