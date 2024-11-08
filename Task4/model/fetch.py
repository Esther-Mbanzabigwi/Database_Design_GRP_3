import requests

# Function to fetch the latest entry from the API
def fetch_latest_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Print raw response for debugging
        print("Raw response:", response.text)
        
        data = response.json()  # Assumes the API returns JSON data
        return data[0] if data else None  # Return the first item if data is a list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError as ve:
        print(f"JSON parsing error: {ve}")
        return None

# Replace 'your_api_endpoint_here' with the actual API URL
api_url = 'https://databases-assignment-g3.onrender.com/docs'

latest_entry = fetch_latest_data(api_url)

if latest_entry:
    print("Latest entry:", latest_entry)
else:
    print("No data found or error occurred.")
