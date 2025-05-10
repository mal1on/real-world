"""
Gets any city name as input and outputs the current temperature for that
city.
"""

import requests

API_KEY = "393a7042d05915ce186f546106ac315a"


def temperature():
    """
    Gets any city name as input and outputs the current temperature for
    that city.
    """
    try:
        city = input("Enter City: ")
        request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(request, timeout=10)
        match response.status_code:
            case 200:
                result = str(round(response.json()["main"]["temp"], 1)) + "°C"
                print(f"Current temperature in {city}: {result}")
            case 401:
                print("API key not valid")
            case 404:
                print(f"City {city} not found")
            case 500:
                print("Internal Server Error")
            case _:
                print(f"Error: {response.status_code}")

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print(
            "There was a connection error. Please check your internet connection."
        )
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")


if __name__ == "__main__":
    temperature()
