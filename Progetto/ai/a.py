import requests
import json

access_token = "EAAJw3ZAhabAUBAMlDWVDIAPV4Cc3OuTZCotDsveEqIOrlFKALMl3mkSkMoCdihscqO9nlFfTL9L9OfmsBeZCTwg4ZBWLI0E9K2yGPtrUeiwd2yRMx9ZCmCnrkSGK9puoPA0jRQlY5alyh59H6I4VH5I6zh61PdnGg8cPfGJ6d1XcdtdQuSC8yHcT2CVzHRpxwidS5rBDLSybWXfSojQ0P5KjEkMj3bsUDjFFIXVkgdtvKgbqZCHnIA"
user_id = "5401356903304090"

url = "https://api.instagram.com/v1/users/{user_id}/media/recent/?access_token={access_token}"

response = requests.get(url)
print(response)
data = json.loads(response.text)

for post in data['data']:
    print(post['images']['standard_resolution']['url'])




# This script uses the requests library to make a GET request to the Instagram API.
# With the access_token and user_id it will return the recent media from that user in json format, 
# then it will iterate over the media and print the image url.
# Please note that you need to have an access_token from Instagram developer account and 
# the user_id of the user to whom you want to get the media.