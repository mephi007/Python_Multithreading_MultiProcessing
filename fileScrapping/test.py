from bs4 import BeautifulSoup
import requests as re


def scrap_through_links(links):
    for link in links:
        directories = ['/']
        aggregate_url_details(link, directories=directories)

def aggregate_url_details(link, directories):
    if directories:
        length_of_directories = len(directories)
        print(length_of_directories)
        # i = 0
        while (length_of_directories > 0):
            # print('printing index : {%d} and length of directories : {%d}', i, length_of_directories)
            if length_of_directories == 0:
                break
            directory = directories[0]
            finding_new_directories(link, directories, directory)
            length_of_directories = length_of_directories - 1
            print('after dec length of directories {}', length_of_directories, type(length_of_directories))
            # i = i+1
    else:
        return
    print(directories)
    aggregate_url_details(link, directories)
    # directories.remove(directories[0])
    print('after removing {}', len(directories))
    if len(directories) == 0:
        return

def finding_new_directories(link, directories, directory):
    if not directories:
        print('aggregated all of the urls, task completed')
        return
    scrapping_url = link + directory
    response = re.get(scrapping_url)
    print('scrapping {} got {}',scrapping_url,response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html5lib')
        for new_directories in soup.find_all('a', href=True):
            new_directory_path = str(new_directories.get('href'))
            if len(new_directory_path) > 1 and new_directory_path.endswith('/'):
                print('found new directory : ', new_directory_path)
                directories.append(scrapping_url+new_directory_path)
    directories.remove(directories[0])
    print('new directories list: ', directories)
    print('after removing {} of length {}', directories, len(directories))
    
if __name__ == '__main__':
    links = ['https://www.mmvideo.fr/dvd/',]
    scrap_through_links(links)
