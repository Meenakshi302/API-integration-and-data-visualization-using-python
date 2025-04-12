# Import required libraries
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Your API key (eg. weather, finance)
api_key = "your_api_key" # put here your unique api key

# Choose your city
city = "Delhi"

#  API endpoint 
url = f"http://api.openweathermap.org/data/2.5/forecast?q=delhi&appid=your_api_keyf&units=metric"

# Send GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
else:
    print("❌ Failed to fetch weather data.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    exit()

# Lists to store extracted data
dates = []
temperatures = []

# Loop through the forecast data
for item in data['list']:

    date = datetime.datetime.fromtimestamp(item['dt'])
    temp = item['main']['temp']  # Temperature in Celsius
    dates.append(date)
    temperatures.append(temp)

# Set up the plot
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

# Create the line plot
sns.lineplot(x=dates, y=temperatures, marker='o', color='teal')

# Add titles and labels
plt.title(f"5-Day Temperature Forecast for delhi", fontsize=16)
plt.xlabel("Date & Time", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)

# Show the plot
plt.show()
