import requests
import argparse

from helpers import download_image, get_filename_and_file_extension


def download_spacex_images(save_folder, launch_id='latest'):
    '''Скачивает изображения SpaceX по id запуска'''

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    image_spacex_urls = response.json()['links']['flickr']['original']

    for number, image in enumerate(image_spacex_urls):
        filename, file_extension = get_filename_and_file_extension(
            image_spacex_urls[number]
        )

        download_image(
            image_spacex_urls[number],
            save_folder,
            f'{filename}{file_extension}'
        )


def main():
    parser = argparse.ArgumentParser(
        description='''Скачивает изображения SpaceX по id запуска'''
    )
    parser.add_argument(
        'launch_id',
        nargs='?',
        default='latest',
        help='id запуска SpaceX'
    )

    parser.add_argument(
        '--save_folder',
        default='images',
        help='Папка для сохранения изображений (по умолчанию images)'
    )

    args = parser.parse_args()

    download_spacex_images(args.save_folder, args.launch_id)


if __name__ == '__main__':
    main()
