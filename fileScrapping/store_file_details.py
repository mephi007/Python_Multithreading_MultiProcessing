from bs4 import BeautifulSoup
import requests as re
import json
import logging 
from file_model import File
from dump_to_db import Dump_to_db


class Store_to_details:
    def __init__(self) -> None:
        logging.basicConfig(filename="logs/std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.dump = Dump_to_db()

    def hit_file_url(self,file_path):
        response = re.get(file_path)
        file_response = json.dumps(response.headers.__dict__['_store'])
        self.logger.info(file_response)
        file_info = json.loads(file_response)
        file_to_db = File(file_url=file_path, content_type=file_info['content-type'][1], content_length=file_info['content-length'][1], last_modified=file_info['last-modified'][1])
        self.logger.info(f'file object going to db: {file_to_db}')
        self.dump.dump_to_db(file_to_db=file_to_db)