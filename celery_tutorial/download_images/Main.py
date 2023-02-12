from .downloadImage import setup_download_dir, getlinks, download_images
import logging
import os
from queue import Queue
from threading import Thread
from time import time




logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            unsplash_api_key, link, category = self.queue.get()
            try:
                download_images(unsplash_api_key, link, category)
            finally:
                self.queue.task_done()

def main():
    ts = time()
    unsplash_api_key = 'oO7pq/1UPXsA3ZYExlMLbQ==yWuEWNqHqwODGO3w'
    categories = ['nature', 'animal', 'building','waterfall']
    links = getlinks(categories)
    # for link, category in links.items():
    #     download_images(unsplash_api_key, link, category)
    queue = Queue()
    # Create 8 worker threads
    for x in range(8):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for link, category in links.items():
        logger.info('Queueing {}'.format(link))
        queue.put((unsplash_api_key, link, category))
        # download_images(unsplash_api_key, link, category)
    queue.join()
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()