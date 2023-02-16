import requests
import shutil
import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)
types = {'image/jpeg', 'image/jpg'}

def getlinks(categories):
    links= {}
    for category in categories:
        url = 'https://api.api-ninjas.com/v1/randomimage?category='+category
        links[url] = category
    return links

def getLinkFromQuery(category):
    url = 'https://api.api-ninjas.com/v1/randomimage?category='+category
    return url

def download_images(unsplash_api_key, link, category):
    for i in range(0,100):
        download_dir = os.path.basename(setup_download_dir(category=category))
        download_path = '{download_dir}/{category}_{index}.jpg'.format(download_dir=download_dir,category=category,index=i)
        logger.info('downloading %s', link)
        response = requests.get(link, headers={'X-Api-Key': unsplash_api_key, 'Accept': 'image/jpg'}, stream=True)
        if response.status_code == requests.codes.ok:
            with open(download_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
                logger.info('Downloaded %s', link)
        else:
            print("Error:", response.status_code, response.text)

def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir(category):
    download_dir = Path(category)
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir