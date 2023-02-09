
import requests
from Ya import YaUploader

TOKEN = ''

if __name__ == '__main__':
    path_to_file = 'readme.md'
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload(path_to_file)