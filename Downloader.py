import pandas as pd
import urllib.request


def url_to_jpg(i, url, file_path):

    filename = '50{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))

    return None


FILENAME = 'lista_down.csv'
FILE_PATH = 'download/'

urls = pd.read_csv(FILENAME)

for i, url in enumerate(urls.values):
    url_to_jpg(i, url[0], FILE_PATH)
