import requests
import os
import argparse

from dotenv import load_dotenv
from helpers import get_filename_and_file_extension, download_image


def download_nasa_apod_images(count, save_folder, api_key):
    '''Скачивает изображения apod по дате'''

    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(url, params)
    response.raise_for_status()
    for number, image_url in enumerate(response.json()):
        link = image_url['url']
        filename, file_extension = get_filename_and_file_extension(link)

        download_image(
            link,
            save_folder,
            f'{filename}{file_extension}'
        )


def main():
    load_dotenv()
    api_key_nasa = os.getenv('API_KEY_NASA')

    parser = argparse.ArgumentParser(
        description='Скачивает изображения apod'
    )
    parser.add_argument(
        '--count',
        type=int,
        default=5,
        help='Сколько нужно скачать изображений, 5 по умолчанию'
    )
    parser.add_argument(
        '--save_folder',
        default='images',
        help='Папка для сохранения изображений (По умолчанию images)'
    )

    args = parser.parse_args()

    download_nasa_apod_images(args.count, args.save_folder, api_key_nasa)


if __name__ == '__main__':
    main()
