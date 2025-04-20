import requests
import argparse

from helpers import download_images, get_file_name_and_file_extension


def download_spacex_images(save_folder, launch_id):
    '''Скачивает изображения SpaceX по id запуска'''

    if launch_id:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        response.raise_for_status()
        launch_id = response.json()['id']
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url)
    response.raise_for_status()
    image_spacex_urls = response.json()['links']['flickr']['original']

    for number, image in enumerate(image_spacex_urls):
        splited_filename = get_file_name_and_file_extension(image_spacex_urls[number])

        download_images(
            image_spacex_urls[number],
            save_folder,
            f'{splited_filename[0]}{splited_filename[1]}')


def main():
    parser = argparse.ArgumentParser(description='''Скачивает изображения
                                                    SpaceX по id запуска''')
    parser.add_argument(
        'launch_id',
        nargs='?',
        default=None,
        help='id запуска SpaceX')

    parser.add_argument(
        '--save_folder',
        default='images',
        help='Папка для сохранения изображений (по умолчанию images)')

    args = parser.parse_args()

    download_spacex_images(args.save_folder, args.launch_id)


if __name__ == '__main__':
    main()
