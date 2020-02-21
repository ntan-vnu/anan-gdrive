from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

file_list = drive.ListFile({'q': "'folder id' in parents and trashed=false"}).GetList()
print(len(file_list))
# print(file_list[0])
file_list.sort()
with open('file_ids.txt', 'wt') as f:
    for it in file_list:
        print it['title']+'.zip', it['id']
        f.write(it['title']+'.zip' + '\t' + it['id'] + '\n')

