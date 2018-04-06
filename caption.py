subscription_key = "d1fe8b11137141ac959ef6bc3fe02429"
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

vision_analyze_url = vision_base_url + "describe"

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

import requests
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Categories,Description,Color'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()