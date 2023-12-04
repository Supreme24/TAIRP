import geocoder
import Pylance
import pycountry
from phone_iso3166.country import phone_country

def get_location_from_ip():
    try:
        # Get IP-based location using the 'geocoder' library
        ip_info = geocoder.ip('me')
        if ip_info:
            print("IP-based Location Information:")
            print("City:", ip_info.city)
            print("Region:", ip_info.region)
            print("Country:", ip_info.country)
            print("Latitude:", ip_info.lat)
            print("Longitude:", ip_info.lng)
        else:
            print("Unable to retrieve location information from the IP address.")
    except Exception as e:
        print("Error occurred:", str(e))

def get_location_from_phone_number(phone_number):
    try:
        # Get country information from the phone number using 'pycountry' and 'phone_iso3166'
        tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
        if tracked:
            print("\nPhone Number-based Location Information:")
            if hasattr(tracked, "official_name"):
                print("Country:", tracked.official_name)
            else:
                print("Country:", tracked.name)
        else:
            print("\nCould not determine location from the phone number.")
    except Exception as e:
        print("Error occurred:", str(e))

if __name__ == "__main__":
    get_location_from_ip()
    
    # Example phone number for tracking location
    phone_number = "+1234567890"  # Replace this with the desired phone number
    get_location_from_phone_number(phone_number)
import geocoder
import pycountry
from phone_iso3166.country import phone_country

def get_location_from_ip():
    try:
        # Get IP-based location using the 'geocoder' library
        ip_info = geocoder.ip('me')
        if ip_info:
            print("IP-based Location Information:")
            print("City:", ip_info.city)
            print("Region:", ip_info.region)
            print("Country:", ip_info.country)
            print("Latitude:", ip_info.lat)
            print("Longitude:", ip_info.lng)
        else:
            print("Unable to retrieve location information from the IP address.")
    except Exception as e:
        print("Error occurred:", str(e))

def get_location_from_phone_number(phone_number):
    try:
        # Get country information from the phone number using 'pycountry' and 'phone_iso3166'
        tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
        if tracked:
            print("\nPhone Number-based Location Information:")
            if hasattr(tracked, "official_name"):
                print("Country:", tracked.official_name)
            else:
                print("Country:", tracked.name)
        else:
            print("\nCould not determine location from the phone number.")
    except Exception as e:
        print("Error occurred:", str(e))

if __name__ == "__main__":
    get_location_from_ip()
    
    # Example phone number for tracking location
    phone_number = "+1234567890"  # Replace this with the desired phone number
    get_location_from_phone_number(phone_number)
