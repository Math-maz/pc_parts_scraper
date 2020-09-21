import requests
from bs4 import BeautifulSoup
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}
def get_product_info(url):
  req = requests.get(url, headers)
  soup = BeautifulSoup(req.content, 'html.parser')
  product_title = soup.find(class_="titulo_det").get_text().strip()
  normal_price = soup.find(class_="preco_normal")
  if(normal_price == None):
    print(f"Produto provavelmente está em promoção, procurando por preço em promoção de: {product_title}")
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
