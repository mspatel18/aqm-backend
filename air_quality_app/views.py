from django.http import JsonResponse
from django.shortcuts import render
from .models import AirQualityData
from datetime import timedelta
from django.utils import timezone
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# def predict_air_quality(request):
#     # Implement your prediction logic here
#     predicted_data = {'particulate_matter': 25.6, 'carbon_monoxide': 1.8}
    # return JsonResponse(predicted_data)

from django.http import JsonResponse
from googleapiclient.discovery import build

#     # Construct the service object for interacting with the Google Sheets API
#     service = build('sheets', 'v4', developerKey=api_key)

#     # Specify the range of data you want to retrieve
#     range_name = 'Sheet1!A1:B10'

#     try:
#         # Make a request to retrieve data from the spreadsheet
#         result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

#         # Process the data
#         values = result.get('values', [])
#         return JsonResponse({'data': values})
#     except Exception as e:
#         # Handle any errors
#         return JsonResponse({'error': str(e)}) 
def get_latest_data(request):
    # Path to the credentials JSON file obtained from Google Cloud Console
    credentials_file = './credentials.json'

    # Scope required for accessing Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Authenticate using the credentials file
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    gc = gspread.authorize(credentials)

    # Open the Google Spreadsheet
    sheet = gc.open_by_key('YOUR_SHEET_ID').sheet1  # Replace 'Your Spreadsheet Name' with actual name

    # Get the latest 30 rows from the spreadsheet
    latest_rows = sheet.get_all_records()[-30:]

    # Format the data as needed
    data = []
    for row in latest_rows:
        data.append({
            'timestamp': row['data'],
            'carbon_monoxide':row['sensor'],
            # 'carbon_monoxide': row['carbon_monoxide'],
            # 'particulate_matter': row['particulate_matter'],
            # 'nitrogen_dioxide': row['nitrogen_dioxide']
        })

    # Return the data as JSON response
    return JsonResponse(data, safe=False)
def get_current_air_quality(request):
    latest_data = AirQualityData.objects.latest('timestamp')
    current_data = {
        'timestamp': latest_data.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'particulate_matter': latest_data.particulate_matter,
        'carbon_monoxide': latest_data.carbon_monoxide,
        'air_quality_index' : latest_data.air_quality_index,
        'nitrogen_dioxide' : latest_data.nitrogen_dioxide, 
    }
    return JsonResponse(current_data)

def get_past_7_days_data(request):
    if request.method == 'GET':
        # Calculate the start and end dates for the past 7 days
        end_date = timezone.now()
        start_date = end_date - timedelta(days=7)
        
        # Fetch air quality data for the past 7 days from the database
        data = AirQualityData.objects.filter(timestamp__range=(start_date, end_date)).values()
        
        # Serialize the data into JSON format
        serialized_data = list(data)

        return JsonResponse(serialized_data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})
