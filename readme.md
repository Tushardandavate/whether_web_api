### Quick Python Weather Tool

A simple and lightweight command-line Python application that fetches real-time, live weather data for any city globally using the OpenWeatherMap API. 

### Features

* Fetches current temperature, "feels like" metrics, relative humidity, and weather condition descriptions.
* Leverages standard Python isolated environments (.venv) for safe, dependency-managed execution.
* Uses the robust requests module to execute secure backend API data transfers.
* Safe error-handling architecture to identify incorrect city spellings or internet connectivity problems.

### Prerequisites

Before running the application, make sure your system has: 

* **Python 3.x** installed.
* A free **OpenWeatherMap API Key** (You can sign up and acquire an access key at https://openweathermap.org).

### Installation & Setup

1. **Clone or navigate to your project workspace directory:** 

bash

cd my_whether_api_project

Use code with caution.
2. **Set up an isolated Virtual Environment (.venv):** 

bash

python3 -m venv .venv

Use code with caution.
3. **Activate the isolated environment sandbox:** 

bash

source .venv/bin/activate

Use code with caution.

*(You should now see (.venv) text visible at the start of your terminal command prompt line).*
4. **Install necessary project requirements:** 

bash

pip install requests

Use code with caution.

### Configuration & Usage

1. Open main.py in your VS Code text editor.
2. Locate the API_KEY placeholder string variables inside the __main__ block entry: 

python

API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

Use code with caution.
3. Swap out the placeholder text with your actual alphanumeric OpenWeather access key token.
4. Run the script directly from your terminal using Python: 

bash

python3 main.py

Use code with caution.
5. Type any city name when prompted (e.g., London, Tokyo, Pune) and press Enter to pull live updates.