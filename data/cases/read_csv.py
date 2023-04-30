import csv
import pytest

with open('./test.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f,skipinitialspace=True)
    for each in data:
        print('data.....',data)



