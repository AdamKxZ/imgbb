# Upload to imgBB
# Written by AdamKxZ

import base64
import requests

# Replace with your API key
apiKey = 'xxxxxx'

print("imgBB API Uploader")
print("API Key: " + apiKey)
fileLocation = input("Enter file location: ")

with open(fileLocation, "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": apiKey,
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)

if res.ok == True:
    print("Server Response: " + str(res.status_code))
    print("Image Successfully Uploaded")
else:
    print("ERROR")
    print("Server Response: " + str(res.status_code))
