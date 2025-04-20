import requests
import os
import argparse

from dotenv import load_dotenv
from helpers import get_file_name_and_file_extension, download_images


def download_nasa_epic_images(save_folder, date):
    '''Скачивает изображения планеты по дате'''

    load_dotenv()
    api_nasa = os.getenv('API_NASA')

    base_url = 'https://api.nasa.gov/EPIC/api/natural'

    if date:
        url = f'{base_url}/date/{date}?api_key={api_nasa}'

    else:
        url = f'{base_url}/available?api_key={api_nasa}'
        response = requests.get(url)
        response.raise_for_status()
        available_dates = response.json()
        if available_dates:
            date = available_dates[-1]
            url = f'{base_url}/date/{date}?api_key={api_nasa}'
        else:
            print('Нет доступных дат')
            return

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    image_urls = []

    for item in data:
        image_name = item['image']
        year, month, day = date.split('-')
        image_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}'
            f'/png/{image_name}.png?api_key={api_nasa}'
        )
        image_urls.append(image_url)

    for number, image in enumerate(image_urls):
        splited_filename = get_file_name_and_file_extension(image_urls[number])
        download_images(
            image_urls[number],
            save_folder,
            f'{splited_filename[0]}{splited_filename[1]}'
        )


def main():
    parser = argparse.ArgumentParser(description='epic')
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

    download_nasa_epic_images(args.save_folder, args.date)


if __name__ == '__main__':
    main()
