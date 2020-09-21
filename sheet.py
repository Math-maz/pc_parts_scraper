import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

def get_client():
  credentials = ServiceAccountCredentials.from_json_keyfile_name("./credentials.json",scope)
  client = gspread.authorize(credentials)
  return client