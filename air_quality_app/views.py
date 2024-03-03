from django.http import JsonResponse
from .models import AirQualityData
from datetime import timedelta
from django.utils import timezone
# def predict_air_quality(request):
#     # Implement your prediction logic here
#     predicted_data = {'particulate_matter': 25.6, 'carbon_monoxide': 1.8}
    # return JsonResponse(predicted_data)

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