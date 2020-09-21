from sheet import get_client

from get_product_info import get_product_info
client = get_client()
sheet = client.open("python").sheet1
sheet_data = sheet.get_all_values()

for i in range(1,len(sheet_data)):
  if "www" in sheet_data[i][0]:
    product_url = sheet_data[i][0]
    product_title,normal_price,discount_price = get_product_info(product_url)
    sheet.update_cell(i+1,2,product_title)
    sheet.update_cell(i+1,3,normal_price)
    sheet.update_cell(i+1,4,discount_price)
print("Busca de preços finalizada!")

