import requests
import json

def get_weather(city_name,api_key):

    # Base url is the endpoints
    base_url = "https://api.openweathermap.org/data/2.5/weather"


    params ={
        'q':city_name,
        'appid':api_key,
        'units':'metric'
    }
    try:
         response = requests.get(base_url,params=params)

         response.raise_for_status()

         # parse the json response into the python  Dict
         data = response.json()

         # Extract the specific information from the nested  JSON structure

         city = data['name']
         country = data['sys']['country']
         temp = data['main']['temp']
         feels_like = data['main']['feels_like']
         humidity = data['main']['humidity']
         description = data['weather'][0]['description']

        # Print formatted results
         print(f"\n🌍 Weather in {city}, {country}:")
         print(f"🌡️  Temperature: {temp}°C (Feels like {feels_like}°C)")
         print(f"☁️  Condition: {description.capitalize()}")
         print(f"💧 Humidity: {humidity}%")

    except requests.exceptions.HTTPError:
        print("\n❌ City not found! Please check the spelling and try again.")
    except requests.exceptions.ConnectionError:
        print("\n❌ Connection error! Check your internet status.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__=='__main__':


    API_KEY = "YOUR API KEY " 

    print("--Python whether project--")

    user_city = input("Enter your city : ").strip()

    if user_city:
        get_weather(user_city, API_KEY)
    else:
        print("City name cannot be blank.")

