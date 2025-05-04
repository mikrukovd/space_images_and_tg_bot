# space_images
Набор скриптов, с помощью которых можноскачивают изображения космоса используя api nasa и spacex, так же есть тг бот для публикации изображений в чат.
## Зависимости
Установка зависимостей:
```bash
pip install -r requrements.txt
```
## Переменные окружения
- `API_KEY__NASA` можно получить [тут](https://api.nasa.gov/).
- `API_KEY_TG_BOT` как создать бота и получить api [тут](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#02).
- `TG_CHAT_ID` как получить id канала [тут](https://docs.leadconverter.su/faq/populyarnye-voprosy/telegram/kak-uznat-id-telegram-gruppy-chata).

## Запуск

### `fetch_spacex_images` 
Запускается командой:
```bash
python fetch_spacex_images.py <id запуска> --save_folder <папка для сохранения изображений>
 ```
Если не указывать id и папку, то будут скачаны изображения с последнего запуска и сохранены в папку `images`(по умолчанию).

### `fetch_nasa_epic_images` 
Запускается командой:
```bash
python fetch_nasa_epic_images.py --date <дата в формате YYYY_MM_DD> --save_folder <папка для сохранения изображений>
```
Если не указывать дату, то будет искать дату ближайшую дату фотографий и сохранены в папку `images`(по умолчанию).

### `fetch_nasa_apod_images`
Запускается командой:
```bash
python fetch_nasa_apod_images.py --date <дата в формате YYYY-MM-DD> --save_folder <папка для сохранения фотографий>
```
Если не указывать дату, то будет искать дату ближайшую дату фотографий и сохранены в папку `images`(по умолчанию).

### `send_images_from_bot`
Запускается командой:
```bash
python send_images_from_bot.py <папка с изображениями> --interval <интервал публикаций в часах>
```
Скрипт работает бесконечно, интервал публикаций по умолчанию 4 часа.

### `helpers`

Содержит вспомогательные функции, которые используются в этих скриптах.

- `download_images` может скачивать изображения по ссылкам  и сохранять в папку
- `get_file_name_and_file_extension` возвращает имя файла и его расширения из ссылки изображения

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
