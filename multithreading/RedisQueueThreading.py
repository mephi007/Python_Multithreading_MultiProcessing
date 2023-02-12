from downloadImage import setup_download_dir, getlinks, download_images
import logging
import os
from queue import Queue
from threading import Thread
from time import time
from redis import Redis
from rq import Queue



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def main():
    ts = time()
    unsplash_api_key = 'oO7pq/1UPXsA3ZYExlMLbQ==yWuEWNqHqwODGO3w'
    categories = ['nature', 'animal', 'building','waterfall']
    links = getlinks(categories)
    # for link, category in links.items():
    #     download_images(unsplash_api_key, link, category)
    queue = Queue(connection=Redis(host='localhost', port=6379))
    # Create 8 worker threads
    for link, category in links.items():
        logger.info('Queueing {}'.format(link))
        queue.enqueue(download_images, unsplash_api_key, link, category)
        # download_images(unsplash_api_key, link, category)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()