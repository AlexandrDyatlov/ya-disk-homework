import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def header(self):    
        return{
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _upload_link(self, file_path):
        get_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.header()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(get_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()
    
    def upload(self, file_path, filename):
        href = self._upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Ok")





