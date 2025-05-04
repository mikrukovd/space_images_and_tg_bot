import os
import time
import random
import argparse
import telegram

from dotenv import load_dotenv


def get_images_from_directiry(directory):
    '''Возвращает словарь с именами файлов изображения'''

    file_extensions = ['.jpg', '.png', '.gif', '.jpeg']
    images = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        extension = os.path.splitext(filename)[1].lower()
        if extension in file_extensions:
            images.append(filepath)
    return images


def publish_image_to_tg(image_path, bot, chat_id,):
    '''Постит изображение в чат'''

    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id, photo=telegram.InputFile(image))


def main():

    load_dotenv()
    tg_token = os.getenv('API_KEY_TG_BOT')
    chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser(description='Публикация фото в тг канал')
    parser.add_argument('directory', help='Путь к папке с изображениями')
    parser.add_argument(
        '--interval',
        type=int,
        default=4,
        help='Интервал публикации изображений в часах'
    )

    args = parser.parse_args()

    directory = args.directory
    interval_seconds = args.interval * 3600

    bot = telegram.Bot(token=tg_token)

    images = get_images_from_directiry(directory)

    while True:
        if not images:
            images = get_images_from_directiry(directory)
            random.shuffle(images)

        image_path = images.pop(0)

        publish_image_to_tg(image_path, bot, chat_id)

        time.sleep(interval_seconds)


if __name__ == '__main__':
    main()
