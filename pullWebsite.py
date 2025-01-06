import requests

# URL of the website
url = 'https://www.example.com'

# Sending a GET request to the website
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Print the HTML content of the page
    print(response.text)
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
