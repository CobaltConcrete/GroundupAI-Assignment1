import requests
import pprint

url = 'http://localhost:10000/generateReport'

file_path = 'M6.csv'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Define the file dictionary; the key ('file' in this case) is the name of the form field
    files = {'file': (file_path, file)}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("File uploaded successfully.")
        data = response.json()
        pprint.pprint(data)   
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
        print(response.text)