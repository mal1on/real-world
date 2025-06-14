"""
Desktop app with a graphical user interface (GUI) getting any city name
as input and outputs the current temperature for that city.
"""

import requests
import FreeSimpleGUI as sg

API_KEY = "393a7042d05915ce186f546106ac315a"


def temperature(city):
    """
    Gets any city name as input and outputs the current temperature for
    that city.
    """
    try:
        request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(request, timeout=10)
        temp, fail = None, None
        match response.status_code:
            case 200:
                temp = str(round(response.json()["main"]["temp"], 1)) + "°C"
            case 401:
                fail = "API key not valid"
            case 404:
                fail = f"City {city} not found"
            case 500:
                fail = "Internal Server Error"
            case _:
                fail = f"Error: {response.status_code}"

    except requests.exceptions.Timeout:
        fail = "The request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        fail = "There was a connection error. Please check your internet connection."
    except requests.exceptions.HTTPError as http_err:
        fail = f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        fail = f"An error occurred: {req_err}"

    return temp, fail


if __name__ == "__main__":
    layout = [
        [sg.Text("Enter City: "), sg.InputText(key="city")],
        [sg.Button("Get Weather"), sg.Button("Exit")],
        [sg.Text("Enter a city name", key="text")],
    ]
    window = sg.Window("Weather App", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Get Weather":
            city = values["city"]
            temp, fail = temperature(city)
            if temp:
                text = f"Current temperature in {city}: {temp}"
            else:
                text = fail
            window["text"].update(text)
            window["city"].update("")
