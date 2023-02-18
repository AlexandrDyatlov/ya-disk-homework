
import requests
from Ya import YaUploader

TOKEN = ''

if __name__ == '__main__':
    
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload( "readme.md", "readme.md")