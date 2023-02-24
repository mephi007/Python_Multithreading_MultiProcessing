from bs4 import BeautifulSoup
import requests as re
import time
import logging 
from store_file_details import Store_to_details
from time import time

class Scrapping_file_urls():
    def __init__(self):
        logging.basicConfig(filename="logs/std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.store_file_info_db = Store_to_details()
        self.extensions  =['jpg', 'mp4', 'ogv', 'webm', 'png']

    def scrap_through_links(self,links):
        # for link in links:
        #     directories = ['/']
        #     aggregate_url_details(link, directories=directories)
        self.aggregate_url_details(directories=links)

    def aggregate_url_details(self,directories):
        if directories:
            length_of_directories = len(directories)
            self.logger.info(f'length of directories list {length_of_directories}\n')
            # i = 0
            while (length_of_directories > 0):
                # self.logger.info('printing index : {%d} and length of directories : {%d}', i, length_of_directories)
                if length_of_directories == 0:
                    break
                directory = directories[0]
                self.finding_new_directories(directories, directory)
                length_of_directories = length_of_directories - 1
                self.logger.info(f'after dec length of directories {length_of_directories}\n')
                # i = i+1
        else:
            return
        self.logger.info(f'traversed directories and back {directories}\n')
        self.aggregate_url_details(directories)
        # directories.remove(directories[0])
        self.logger.info(f'after traversing the list of directories {directories}\n')
        if len(directories) == 0:
            return

    def finding_new_directories(self,directories, directory):
        if not directories:
            self.logger.info(f'aggregated all of the urls, task completed')
            return
        scrapping_url = directory
        response = re.get(scrapping_url)
        self.logger.info(f'scrapping {scrapping_url} got {response.status_code}\n')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html5lib')
            for new_directories in soup.find_all('a', href=True):
                new_directory_path = str(new_directories.get('href'))
                length_new_url = len(new_directory_path)
                self.logger.info(f'new_directory : {new_directory_path}')
                if new_directory_path.startswith('?') or new_directory_path.startswith('/'):
                    continue
                elif len(new_directory_path) > 1 and new_directory_path.endswith('/'):
                    self.logger.info(f'found new directory : {new_directory_path}\n')
                    new_url = scrapping_url+new_directory_path
                    if new_url not in directories:
                        directories.append(scrapping_url+new_directory_path)
                elif new_directory_path.rsplit('.',1)[1] and new_directory_path.rsplit('.',1)[1] in self.extensions:
                    # self.logger.info(f'found new file {scrapping_url+new_directory_path}\n')
                    file_path = scrapping_url+new_directory_path
                    self.store_file_info_db.hit_file_url(file_path)
        directories.remove(directories[0])
        # self.logger.info(f'new directories list: {}', directories)
        self.logger.info(f'after removing {directories} of length {len(directories)}\n')


    
if __name__ == '__main__':
    ts = time()
    links = ['https://www.mmvideo.fr/dvd/',]
    scrap_file_urls = Scrapping_file_urls()
    scrap_file_urls.scrap_through_links(links)
    logging.info('Took %s seconds', time() - ts)
