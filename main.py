import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup

def get_product_info(url):
  req = requests.get(url, headers)
  soup = BeautifulSoup(req.content, 'html.parser')
  product_title = soup.find(class_="titulo_det").get_text().strip()
  normal_price = soup.find(class_="preco_normal")
  # discount_price = soup.select(".preco_desconto span span strong")
  if(normal_price == None):
    print("Produto provavelmente está em promoçao")
    normal_price = soup.find(class_="preco_desconto-cm")
    discount_price = soup.find(class_="preco_desconto_avista-cm")
    if(normal_price != None):
      normal_price = normal_price.get_text().strip()
    if(discount_price != None):
      discount_price = discount_price.get_text().strip()
  else:
    normal_price = normal_price.get_text().strip()
    discount_price = soup.select(".preco_desconto span span strong")[0].get_text().strip()
  return product_title,normal_price,discount_price
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("./credentials.json",scope)
client = gspread.authorize(credentials)
sheet = client.open("python").sheet1

sheet_data = sheet.get_all_values()

for i in range(1,len(sheet_data)):
  if "www" in sheet_data[i][0]:
    product_url = sheet_data[i][0]
    product_title,normal_price,discount_price = get_product_info(product_url)
    sheet.update_cell(i+1,2,product_title)
    sheet.update_cell(i+1,3,normal_price)
    sheet.update_cell(i+1,4,discount_price)


