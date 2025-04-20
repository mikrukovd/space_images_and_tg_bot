import os
import requests

from urllib.parse import urlsplit


def download_images(image_url, save_folder, filename):
    '''Создает папку и скачивает картинку с сайта'''

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    filepath = os.path.join(save_folder, filename)

    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_file_name_and_file_extension(image_url):
    '''Возвращает имя и расширение файла из ссылки'''

    return os.path.splitext(os.path.split(urlsplit(image_url).path)[1])
