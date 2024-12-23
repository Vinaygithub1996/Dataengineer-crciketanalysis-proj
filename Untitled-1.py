

import requests

# Send a GET request to the API
response = requests.get("https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen")

# Parse the JSON response
data = response.json()

# Display the data
print(data)
