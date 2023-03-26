import csv

import PyPDF2
import pandas as pd

pdf_file = open('file.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

rows = []

for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text = page.extract_text()
    rows.extend(text.split('\n'))

new_list = []
for item in rows:
    cols = item.split()
    col_list = [x for i, x in enumerate(cols) if i != 4]
    new_list.append(col_list)

with open('my_csv.csv', 'w') as file:
    writer = csv.writer(file)

    for row in new_list:
        writer.writerow(row)

print("Done")
