
from bs4 import BeautifulSoup
import requests
import pandas as pd


class ReadPage:

  def __init__(self, url) -> None:
    self.url = url

  def __get_page(self):
    response = requests.get(self.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
  
  def find_table_rows(self):
    soup = self.__get_page()
    product_rows = soup.findAll('tr')
    return product_rows

  

  
