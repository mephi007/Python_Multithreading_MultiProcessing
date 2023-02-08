from downloadImage import setup_download_dir, getlinks, download_images
import logging
import os
from queue import Queue
from threading import Thread
from time import time
from concurrent.futures import ThreadPoolExecutor
import requests
import shutil
import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def downloadImage(category):
    url = 'https://api.api-ninjas.com/v1/randomimage?category='+category
    unsplash_api_key = 'oO7pq/1UPXsA3ZYExlMLbQ==yWuEWNqHqwODGO3w'
    for i in range(0,5):
        download_dir = os.path.basename(setup_download_dir(category=category))
        download_path = '{download_dir}/{category}_{index}.jpg'.format(download_dir=download_dir,category=category,index=i)
        logger.info('downloading %s', url)
        response = requests.get(url, headers={'X-Api-Key': unsplash_api_key, 'Accept': 'image/jpg'}, stream=True)
        if response.status_code == requests.codes.ok:
            with open(download_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
                logger.info('Downloaded %s', url)
        else:
            print("Error:", response.status_code, response.text)


def main():
    ts = time()
    
    categories = ['nature', 'animal', 'building','waterfall']

    # links = getlinks(categories)
    
    with ThreadPoolExecutor() as executor:
        executor.map(downloadImage, categories, timeout=30)

    # for link, category in links.items():
    #     logger.info('Queueing {}'.format(link))
    #     download_images(unsplash_api_key, link, category)
     

    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()