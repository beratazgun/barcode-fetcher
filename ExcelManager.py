import pandas as pd

class ExcelManager:
  def __init__(self) -> None:
    pass

  def create_excel(self, data):
    df = pd.DataFrame(data)
    df.to_excel('urunler.xlsx', index=False, engine='openpyxl')
    print('Excel dosyası oluşturuldu.')
    
  def read_excel(self):
    df = pd.read_excel('urunler.xlsx')
    return df