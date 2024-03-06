from django.urls import path
from . import views

urlpatterns = [
    # path('predict/', views.predict_air_quality),
    # path('get-spreadsheet-data/',views.get_spreadsheet_data),
    path('latest-data/',views.get_latest_data),
    path('current/', views.get_current_air_quality),
    path('past-7-days/', views.get_past_7_days_data)
]
