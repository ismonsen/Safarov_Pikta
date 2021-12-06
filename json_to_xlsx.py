from openpyxl import Workbook
import json
book = Workbook()
sheet = book.active
book.remove(sheet)
for i in range(1, 4):
    sheet = book.create_sheet(f'JSON{i}')
    sheet.title = f'JSON{i}'
    with open(f'test{i}.json', encoding='utf8') as file:
        data = json.load(file)
        headers = {}
        key = 1
        for el in data['headers']:
            headers[key] = el['properties']['QuickInfo']
            key += 1
        sheet.append(headers)
        mas_lines = {}
        columns_counter = 0
        for el in data['values']:
            line = {'10': 1, '7': 2, '9': 3, '2': 4}
            mas_lines[line.get(el['properties']['MaxLength'])] = el['properties']['Text']
            columns_counter += 1
            if columns_counter > 3:
                sheet.append(mas_lines)
                columns_counter = 0
                mas_lines.clear()
book.save('JSON_To_Excel.xlsx')
book.close()
