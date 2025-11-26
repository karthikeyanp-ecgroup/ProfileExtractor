import gspread
from google.oauth2.service_account import Credentials

def write_to_sheet(data):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)

    sheet = client.open("Candidate Database").sheet1

    sheet.append_row([
        data.get("full_name"),
        data.get("email"),
        data.get("phone"),
        data.get("skills"),
        data.get("total_experience_years"),
        data.get("last_company"),
        data.get("education"),
        data.get("notice_period")
    ])
