import requests

def fetch_data(location, API_KEY):

    URL =  f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=us&key={API_KEY}&contentType=json"
    data = requests.request("GET", URL)

    if data.status_code != 200:
        return {"Unexpected Status code": data.status_code}
    
    else:
        data = data.json()
        if data["address"] == "None":
            return {"Unexpected error": "Location empty"}
        
        return data