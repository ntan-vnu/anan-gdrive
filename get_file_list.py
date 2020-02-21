from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

file_list = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()