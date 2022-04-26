import requests


def get_token():
    with open('token.txt', encoding='utf-8') as file:
        token = file.readline()
    return token


class YaUploader:
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _upload_link(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params, headers=self.get_headers())
        return response.json()

    def upload(self, file_path: str):
        href = self._upload_link(file_path).get('href')
        open_file = open(file_path, 'rb')
        if not href:
            return False

        response = requests.put(href, data=open_file)
        if response.status_code == 201:
            print(f'Файл {file_path} загружен на Яндекс Диск')
            return True


def main():
    path_to_file = 'text1.txt'
    token = get_token()
    uploader = YaUploader(token)
    uploader.upload(path_to_file)


if __name__ == '__main__':
    main()
