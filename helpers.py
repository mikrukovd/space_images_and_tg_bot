import os
import requests

from urllib.parse import urlsplit


def download_image(image_url, save_folder, filename):
    '''Создает папку и скачивает картинку с сайта'''

    os.makedirs(save_folder, exist_ok=True)

    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    filepath = os.path.join(save_folder, filename)

    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_filename_and_file_extension(image_url):
    '''Возвращает имя и расширение файла из ссылки'''
    splited_url = urlsplit(image_url).path
    filename = os.path.split(splited_url)[1]
    splited_filename = os.path.splitext(filename)

    return splited_filename
