import requests, os, re
u = "https://docs.google.com/spreadsheet/ccc?key=1JOqzBhFVSCzE7Ayakb8pUVoa_QtPSjje"
def main():
    url = "https://docs.google.com/spreadsheet/ccc?key=1r4XJiqsiedLxNmJMv6m_MIVo541ikeFeSWQ1psGFQ6A&output=csv"
    data = requests.get(url).content

    with open("file.csv", "wb") as f:
        f.write(data)

def f():
    files = os.listdir("links")
    pattern = r"/d/([-\w]+)"
    print(files)
    for file in files:
        with open("links/"+file,'r') as f:
            lines = f.readlines()
        for line in lines:
            match = re.search(pattern, line)
            if match:
                token = match.group(1)
                with open(file.replace(".txt", "-tokens.txt"), 'a') as g:
                    g.write(token+'\n')

import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

url = "https://drive.google.com/drive/folders/1WMMzK-6n8VukzHHr_CEWwWAUV7CSVcZG?usp=sharing"
folder_id = '1WMMzK-6n8VukzHHr_CEWwWAUV7CSVcZG'


gauth = GoogleAuth()
gauth.LocalWebserverAuth("./creds.json")
drive=GoogleDrive(gauth)

file_list = drive.ListFile({'q': f"'{folder_id}' in parents"}).GetList()

if not file_list:
    print('No files found.')
else:
    print('Files:')
    for file in file_list:
        print(f"{file['title']} ({file['id']})")


