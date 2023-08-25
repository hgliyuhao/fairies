import json
import numpy as np
from tqdm import tqdm
import csv
import orjson
import xlsxwriter


def write_json(filename, res, isIndent=False, isLine=False):
    """
    Writes a list or dict to a JSON file.
    """
    mode = 'a' if isLine else 'w'
    with open(filename, mode, encoding='utf-8') as json_file:
        if isIndent:
            json.dump(res, json_file, ensure_ascii=False, indent=4)
        else:
            if isinstance(res, (list, dict)) and not isLine:
                json.dump(res, json_file, ensure_ascii=False)
            else:
                for formatted_instance in res:
                    json_str = json.dumps(formatted_instance,
                                          ensure_ascii=False)
                    json_file.write(json_str + '\n')


def write_orjson(fileName, res):
    """
    Writes data to a file using orjson.
    """
    with open(fileName, 'wb') as json_file:
        json_file.write(orjson.dumps(res))


def write_txt(fileName, lists, model='normal'):
    """
    Writes a list of data to a text file.
    """
    mode = 'a' if model != 'normal' else 'w'
    with open(fileName, mode, encoding='utf8') as f:
        for i in tqdm(lists):
            f.write(str(i) + '\n')


def write_npy(fileName, lists):
    """
    Writes data to a numpy file.
    """
    np.save(fileName, lists)


def write_csv(filename, data):
    """
    Writes a list of lists to a CSV file.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in tqdm(data):
            writer.writerow(i)


def write_excel(filename, data, sheet_name='Sheet1'):
    """
    Writes a list of lists to an Excel file.
    """
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet(sheet_name)

    for i, row_data in enumerate(data):
        for j, cell_data in enumerate(row_data):
            worksheet.write(i, j, cell_data)

    workbook.close()