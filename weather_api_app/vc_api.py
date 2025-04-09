import requests

def fetch_data(location):

    URL =  f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=us&key=UEFSR67YAH9UT9QUT52UKPV8B&contentType=json"
    data = requests.get(URL)
    if data.status_code == "200":
        data = data.json()

        print(data)