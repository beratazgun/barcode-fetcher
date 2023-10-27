from ExcelManager import ExcelManager
import pandas as pd
from FinderInTables import FinderInTables


sum_of_data = []
page = 1
while page < 1293:
    url = f'https://www.netdata.com/netsite/d9d458c0/tablo?p={page}'
    finderInTables = FinderInTables()
    data = finderInTables.for_loop_in_table_rows(url)
    sum_of_data += data
    page += 1
    print('Page:', page)


excelManager = ExcelManager()
excelManager.create_excel(sum_of_data)

