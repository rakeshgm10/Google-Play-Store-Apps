import requests

url = "https://example.com/path/to/googleplaystore.csv"  # Replace with the actual URL
response = requests.get(url)

with open("googleplaystore.csv", "wb") as file:
    file.write(response.content)

print("Download complete.")
