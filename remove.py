import os
import sqlite3
import requests

from dotenv import load_dotenv

# To load environment variables.
load_dotenv()


def get_emby_api_key():
    return os.getenv("EMBY_API_KEY")


def get_emby_host_url():
    return os.getenv("EMBY_HOST_URL")


def get_db_file():
    return os.getenv("DATABASE_FILE")


# Notifies a item (movie or tv show episode needs to be removed)
def post_emby_to_remove(media_ids_to_remove:list):
    host_url = get_emby_host_url()
    api_key = get_emby_api_key()

    for id in media_ids_to_remove:
        delete_url = f'{host_url}/emby/Items/?Ids={id}&api_key={api_key}'

        print(delete_url)
        print(requests.delete(url=delete_url).content)


def get_items_to_remove():
    conn = sqlite3.connect(get_db_file())

    cursor = conn.execute(
        """
        SELECT MediaItems.Id
        FROM MediaItems
        JOIN UserDatas ON UserDatas.UserDataKeyId = MediaItems.UserDataKeyId
        WHERE UserDatas.played = true AND MediaItems.MediaType != 2
        """
    )
    watched_media_ids = list(map(lambda row: row[0], cursor.fetchall()))

    conn.close()

    return watched_media_ids


def main():
    ids_to_remove = get_items_to_remove()
    print(ids_to_remove)
    post_emby_to_remove(ids_to_remove)


if __name__ == '__main__':
    main()
