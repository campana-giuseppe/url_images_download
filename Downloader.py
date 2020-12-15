import pandas as pd
import urllib.request
#downloader of images from a list of urls on a cvs file

def url_to_jpg(i, url, file_path):

    filename = '{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))

    return None


FILENAME = 'lista_down.csv' #file name csv with links
FILE_PATH = 'download/'   #folder name to save images (placed in the same folder of py file)

urls = pd.read_csv(FILENAME)

for i, url in enumerate(urls.values):
    url_to_jpg(i, url[0], FILE_PATH)
