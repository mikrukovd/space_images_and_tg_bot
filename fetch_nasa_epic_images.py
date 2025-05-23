import requests
import os
import argparse

from urllib.parse import urlencode
from datetime import datetime
from dotenv import load_dotenv
from helpers import get_filename_and_file_extension, download_image


def download_nasa_epic_images(save_folder, date, api_key):
    '''Скачивает изображения планеты по дате'''

    base_url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}

    if date:
        url = f'{base_url}/date/{date}'

    else:
        url = f'{base_url}/available'
        response = requests.get(url, params)
        response.raise_for_status()
        available_dates = response.json()

        if available_dates:
            date = available_dates[-1]
            url = f'{base_url}/date/{date}'

        else:
            print('Нет доступных дат')
            return

    response = requests.get(url, params)
    response.raise_for_status()
    image_urls = []

    for content in response.json():
        image_name = content['image']
        launch_date = datetime.fromisoformat(date)
        year = launch_date.strftime('%Y')
        month = launch_date.strftime('%m')
        day = launch_date.strftime('%d')
        image_base_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}'
            f'/png/{image_name}.png'
        )
        image_url = f'{image_base_url}?{urlencode(params)}'
        image_urls.append(image_url)

    for link in image_urls:
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
        description='Скачивает изображения epic'
    )
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

    download_nasa_epic_images(args.save_folder, args.date, api_key_nasa)


if __name__ == '__main__':
    main()
