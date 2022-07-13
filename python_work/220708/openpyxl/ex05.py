from openpyxl import Workbook
import numpy as np

wb = Workbook()  # 새로운 xlsx 파일을 만들어라
ws = wb.active

# index = 1
for r in range(1, 11):
    for c in range(1, 11):
        ws.cell(row=r, column=c).value = np.random.randint(0, 100)
        # index += 1

wb.save('b.xlsx')  # ('b.xlsx')파일로 저장하라
wb.close()
