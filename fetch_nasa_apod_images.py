import requests
import os
import argparse

from dotenv import load_dotenv
from helpers import get_file_name_and_file_extension, download_images


def download_nasa_apod_images(date, save_folder):
    '''Скачивает изображения apod по дате'''

    load_dotenv()
    api_nasa = os.getenv('API_NASA')

    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_nasa}

    if date:
        params['date'] = date

    response = requests.get(url, params)
    response.raise_for_status()
    image_url = response.json()['url']

    splited_filename = get_file_name_and_file_extension(image_url)

    download_images(
        image_url,
        save_folder,
        f'{splited_filename[0]}{splited_filename[1]}'
    )


def main():
    parser = argparse.ArgumentParser(description='Скачивает изображения apod по дате')
    parser.add_argument(
        '--date',
        type=str,
        help='Дата в формате YYYY-MM-DD'
    )
    parser.add_argument(
        '--save_folder',
        default='images',
        help='Папка для сохранения изображений (По умолчанию images)'
    )

    args = parser.parse_args()

    download_nasa_apod_images(args.date, args.save_folder)


if __name__ == '__main__':
    main()
