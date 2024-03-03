# air_quality_app/management/commands/populate_air_quality_data.py
# from faker import Faker
from django.core.management.base import BaseCommand
from django.utils import timezone
from air_quality_app.models import AirQualityData
from random import uniform
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the database with sample air quality data'

    def handle(self, *args, **kwargs):
        # Generate and save sample air quality data

        # fake = Faker()
        for i in range(7):
    # Generate a timestamp for the current day
            current_date = timezone.now() - timedelta(days=i)
            
            # Generate air quality data for each hour of the day
            for hour in range(24):
                # Generate timestamp for the current hour
                timestamp = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
                
                # Generate random values for particulate matter and carbon monoxide
                particulate_matter = uniform(0, 100)
                carbon_monoxide = uniform(0, 100)
                air_quality_index = uniform(0,100)
                nitrogen_dioxide = uniform(0,100)
                
                # Create an instance of AirQualityData model
                air_quality_data = AirQualityData(
                    timestamp=timestamp,
                    particulate_matter=particulate_matter,
                    carbon_monoxide=carbon_monoxide,
                    air_quality_index=air_quality_index,
                    nitrogen_dioxide = nitrogen_dioxide
                )
                
                # Save the instance to the database
                air_quality_data.save()
