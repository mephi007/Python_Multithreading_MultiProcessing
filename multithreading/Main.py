import logging
import os
from time import time

from downloadImage import setup_download_dir, getlinks, download_images

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    ts = time()
    unsplash_api_key = 'oO7pq/1UPXsA3ZYExlMLbQ==yWuEWNqHqwODGO3w'
    categories = ['nature', 'animal', 'building','waterfall']
    # download_dirs = setup_download_dirs(categories)
    links = getlinks(categories)
    # links = get_links(unsplash_api_key, categories)
    for link, category in links.items():
        download_images(unsplash_api_key, link, category)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()