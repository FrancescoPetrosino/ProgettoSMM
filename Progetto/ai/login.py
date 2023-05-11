# To obtain an access token for the Instagram API, you will need to register your application
# on the Instagram Developer Platform. Here are the basic steps to get an access token:

# 1 - Go to the Instagram Developer Platform (https://www.instagram.com/developer/) and log in with your Instagram account.
# 2 - Register a new application by clicking on the "Register a New Client" button.
# 3 - Fill in the required information for your application, such as the name, description, and website URL.
# 4 - In the "Security" tab, you will be prompted to enter a valid redirect URI. This is the URI that Instagram will redirect the user to after they authorize your application.
# Once your application is registered, you will be provided with a client_id and client_secret.
# To use these credentials to get the access token you can use the following script:

import requests
import json
import re

client_id = "687046999567365"
client_secret = "793f8b29e7bf8663e48e3b0643f566ea"
redirect_uri = "https://www.example.com/oauth-callback"

url = f"https://api.instagram.com/oauth/authorize/?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=public_content"

response = requests.get(url)

if response.text and response.text.strip():
    # do something with data
    json_string = re.sub(r'([\n\r\t]+)', '', response.text)
    json_string = re.sub(r'([ ]{2,})', '', json_string)
    data = json.loads(response.text)
else:
    print("Invalid json or empty json string")
    data = ""


data = json.loads(json_string)

code = data['code']

url = f"https://api.instagram.com/oauth/access_token"

payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "code": code,
    "grant_type": "authorization_code"
}

response = requests.post(url, data=payload)
data = json.loads(response.text)

access_token = data['access_token']

# This script uses the requests library to make a GET request to the Instagram API to authorize the application and get the code. Then it will make a post request to the access_token endpoint providing the client_id, client_secret, redirect_uri, code and grant_type.
# This way you will receive an access_token that you can use to make authorized requests to the Instagram API.
# Please note that to make a request to access_token endpoint you need to have a valid redirect_uri in your application that Instagram can redirect the user after the authorization.
# It's important to mention that Instagram has a rate limit to the number of requests you can do to the API and with this access_token, you can make up to 5,000 requests per hour.