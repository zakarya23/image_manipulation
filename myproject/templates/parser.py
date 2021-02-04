from bs4 import BeautifulSoup
from PIL import Image
import csv 
import urllib.request
import os 
import requests 
# Use a databse to sabe the url anf then parse from that? 
page = requests.get('http://127.0.0.1:8000/#')

# with open('templates/home.html') as fp: 
#     soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup(page.text, 'html.parser')

# soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

# print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))
image = (soup.find_all('video'))
images = soup.find_all('img')

example = images[0]
image_link = soup.find_all('p')

print(soup.find_all('img'))
f = csv.writer(open('images.csv', 'w'))
f.writerow(image)

soup2 = BeautifulSoup(page.text, 'html.parser')
print(soup2.find_all('img'))

def download_image(url):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    urllib.request.urlretrieve(url,os.path.join('image.png', name))