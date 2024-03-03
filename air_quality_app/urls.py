from django.urls import path
from . import views

urlpatterns = [
    # path('predict/', views.predict_air_quality),
    path('current/', views.get_current_air_quality),
    path('past-7-days/', views.get_past_7_days_data)
]
