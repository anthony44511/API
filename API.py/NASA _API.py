import requests
import os
import shutil
os.system('cls')

api_key ="1khS1UrLZ8MWfQNGLvBJNmB0H4GWxZFfazJKcWSs"
params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=1khS1UrLZ8MWfQNGLvBJNmB0H4GWxZFfazJKcWSs", params=params)
request = response.request
response.json()
photos = response.json()["photos"]



image_url = photos[16]["img_src"]
image_url_2 = photos[21]["img_src"]
image_url_3 = photos[6]["img_src"]

filename = image_url.split("/")[-1]
filename2 = image_url_2.split("/")[-1]
filename3 = image_url_3.split("/")[-1]

r = requests.get(image_url, stream = True)
r2 = requests.get(image_url_2, stream = True)
r3 = requests.get(image_url_3, stream = True)

if r.status_code == 200:
    r.raw.decode_content = True

    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldnt be retreived')

if r2.status_code == 200:
    r2.raw.decode_content = True

    with open(filename2,'wb') as f:
        shutil.copyfileobj(r2.raw, f)

    print('Image sucessfully Downloaded: ',filename2)
else:
    print('Image Couldnt be retreived')

if r3.status_code == 200:
    r3.raw.decode_content = True

    with open(filename3,'wb') as f3:
        shutil.copyfileobj(r3.raw, f3)

    print('Image sucessfully Downloaded: ',filename3)
else:
    print('Image Couldnt be retreived')

response.json()
photos = response.json()["photos"]
print(response.text)
# print(request.headers)
print(response.url[1])
print(response.headers)
# ['image_url']


