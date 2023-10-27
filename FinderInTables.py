
from ReadPage import ReadPage

class FinderInTables: 
  def __init__(self) -> None:
    pass

  def __find_barcode_element(self, product_row):
    barcode_element = product_row.find('td', {'data-title': 'BarcodeId'})
    return barcode_element

  def __find_product_name_element(self, product_row):
    product_name_element = product_row.find('td', {'data-title': 'ProductName'})
    return product_name_element
  
  def for_loop_in_table_rows(self, url):
    table_rows = ReadPage(url).find_table_rows()
    data = []
    for product_row in table_rows:
      barcode_element = self.__find_barcode_element(product_row)
      product_name_element = self.__find_product_name_element(product_row)

      if barcode_element and product_name_element:
        barcode_id = barcode_element.find('span').text
        product_name = product_name_element.find('span').text
        data.append({'BarcodeId': barcode_id, 'ProductName': product_name})

        print('BarcodeId:', barcode_id, 'ProductName:', product_name)
    return data