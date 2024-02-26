import argparse
import folium
import os
import phonenumbers
import sys
from colorama import init, Fore
from phonenumbers import geocoder, timezone, carrier
from opencage.geocoder import OpenCageGeocode


def process_number(number):
    try:
        result = {}
        parsed_number = phonenumbers.parse(number)

        result['international_format'] = phonenumbers.format_number(parsed_number,
                                                                    phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        country_code = parsed_number.country_code
        result['country_code'] = "+" + str(country_code)

        result['time_zone'] = list(timezone.time_zones_for_number(parsed_number))

        country = geocoder.country_name_for_number(parsed_number, "en")
        result['country'] = country if country else "Unknown"

        location = geocoder.description_for_number(parsed_number, "en")
        result['region'] = location if location else "Unknown"

        service_provider = carrier.name_for_number(parsed_number, 'en')
        result['service_provider'] = service_provider if service_provider else "Unknown"

        return result

    except Exception as e:
        return str(e)


def get_approx_coordinates(location):
    try:
        coder = OpenCageGeocode("0c922f66970d48028e0ac31be4cc15c6")
        query = location
        results = coder.geocode(query)
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude
    except Exception as e:
        print(f"Error: {e}")
        return None

