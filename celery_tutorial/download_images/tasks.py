import random
from celery import shared_task
from .downloadImage import setup_download_dir, getlinks, download_images
from .Main import main
import logging
import os
from queue import Queue
from threading import Thread
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


@shared_task
def add(x, y):
    # Celery recognizes this as the `movies.tasks.add` task
    # the name is purposefully omitted here.
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as the `sum_list_numbers` task
    return sum(numbers)


@shared_task(name='downloadImages')
def downloadImages():
    ts = time()
    unsplash_api_key = 'oO7pq/1UPXsA3ZYExlMLbQ==yWuEWNqHqwODGO3w'
    categories = ['nature', 'animal', 'building','waterfall']
    links = getlinks(categories)
    for link, category in links.items():
        download_images(unsplash_api_key, link, category)
    logging.info('Took %s seconds', time() - ts)

@shared_task(name='downloadImagesWithThreading')
def downloadImagesWithThreading():
    main()