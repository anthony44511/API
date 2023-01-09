from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from flask import Flask, request

app = Flask(__name__)

@app.route('/store-emails', methods=['POST'])
def store_emails():
    # Authenticate the API key and create a Sheets API service client
    credentials = Credentials.from_authorized_user_info(info=request.json)
    service = build('sheets', 'v4', credentials=credentials)

    # Retrieve the gym instructor emails
    sheet_id = request.json['sheet_id']
    result = service.spreadsheets().values().get(spreadsheetId=sheet_id, range='A1:A').execute()
    emails = result.get('values', [])

    # Store the emails in the Google Sheets document
    body = {
        'values': [[email] for email in emails]
    }
    result = service.spreadsheets().values().append(spreadsheetId=sheet_id, range='A1', insertDataOption='INSERT_ROWS', valueInputOption='RAW', body=body).execute()

    return 'Success'
