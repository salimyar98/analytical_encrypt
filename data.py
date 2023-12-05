"""
Модуль data.py используется для хранения алфавита
и кодировки в словаре coding_alphabet.
coding_alphabet_reverse - обратный словарь, для
упрощения расшифровки теска.
matrix_option_list - словарь с матрицами,
которые используются для вычислений.
"""
import csv

matrix_option_list = {}

with open('matrix.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    for row in reader:
        key = int(row[0].strip())
        values_str = row[1].strip()
        values_list = eval(values_str)
        matrix_option_list[key] = values_list[0]

coding_alphabet = {chr(1039 + i): i for i in range(1, 33)}

coding_alphabet_reverse = {i: chr(1039 + i) for i in range(1, 33)}
