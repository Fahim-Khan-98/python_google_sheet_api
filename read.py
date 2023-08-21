import argparse

from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
cred = None
cred = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1FwjQEgPzYzKGQsk05vYLzce2DHsfMoKeY2vG7elHW9I'
 

service = build('sheets', 'v4', credentials=cred)
# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="sales1!A1:G13").execute()
values = result.get('values', [])
aoa = [["2/7/2027","tasfi","Islam","Chandpur","Dupno",5000,4352]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range="sales1!A14" , valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
print(request)

