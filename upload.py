from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)


# Importing os and glob to find all PDFs inside subfolder
import glob
import os

def upload(file_list, log_file):
	for fff in file_list:
		basename = os.path.basename(fff)
		os.system('zip -r %s.zip %s'%(basename, fff))
		print(basename, 'zipped...')
		with open(basename+'.zip', "r") as f:
			file_drive = drive.CreateFile({'title': basename,
										   'parents': [{'id': '#folder id'}]})
			file_drive.SetContentFile(basename+'.zip')
			file_drive.Upload()
		print(basename+'.zip', 'uploaded...')
		log_file.write(fff+'\n')
		os.system('rm %s.zip'%(basename))


IN_DIR = '/home/ntan/sdc1/nlst-ct/'

if __name__ == "__main__":
	uploaded_list = []
	if os.path.exists('log_uploaded.txt'):
		uploaded_list = [it.strip() for it in open('log_uploaded.txt').readlines()]
	print(len(uploaded_list), 'uploaded...')
	folders = [os.path.abspath(it) for it in glob.glob(IN_DIR + '*') if it not in uploaded_list]
	folders.sort()
	print(len(folders), 'uploading...')


	log_file = open('log_upload.txt', 'at')
	upload(folders, log_file)
	log_file.close()
	pass