# -*- coding: utf-8 -*-

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import os
import argparse
import json
import glob

mimetypes = {
    # Drive Document files as MS Word files.
    'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',

    # Drive Sheets files as MS Excel files.
    'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    # etc.
}

def download_file(g_drive, dest_folder, file_id):
    if dest_folder == None:
        dest_folder = './'
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    else:
        assert dest_folder + 'existed.'
    
    try:
        m_file = g_drive.CreateFile({'id': file_id})
        # json.dump(m_file, open('file_meta.json', 'w'), indent=4)
        # print(m_file)
        file_name = m_file['title']
        if m_file['mimeType'] in mimetypes:
            m_file.GetContentFile(os.path.join(dest_folder, file_name),
                                        mimetype=mimetypes[m_file['mimeType']])
        else:
            m_file.GetContentFile(os.path.join(dest_folder, file_name))
        print(file_name, m_file['id'])
    except:
        print('Fail to download [' + file_name + '] [' + file_id + '] to ' + dest_folder)
    pass

def upload_file(g_drive, dest_folder_id, file_name):
    basename = os.path.basename(file_name)

    try:
        m_file = g_drive.CreateFile({'title': basename})
        if dest_folder_id != None:
            m_file['parents'] = [{'id': dest_folder_id}]
        m_file.SetContentFile(file_name)
        m_file.Upload()
        print(basename, m_file['id'])
    except:
        print('Fail to upload [' + file_name + '] to folder ' + dest_folder_id)
    pass

def download_folder(g_drive, dest_folder, folder_id):
    file_list = g_drive.ListFile({'q': "'%s' in parents and trashed=false"%(folder_id)}).GetList()
    file_list.sort()
    
    if dest_folder == None:
        dest_folder = './'
    folder_name = g_drive.CreateFile({'id': folder_id})['title']
    dest_folder = os.path.join(dest_folder, folder_name)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    else:
        assert dest_folder + 'existed.'

    m_files = []
    m_folders = []
    for it in file_list:
        if it['mimeType']=='application/vnd.google-apps.folder':
            m_folders.append(it)
        else:
            m_files.append(it)
    
    for it in m_files:
        download_file(g_drive, dest_folder, it['id'])
    for it in m_folders:
        download_folder(g_drive, dest_folder, it['id'])
    pass

def upload_folder(g_drive, dest_folder_id, folder_name):
    folder_name = os.path.realpath(folder_name)
    basename = os.path.basename(folder_name)
    
    if dest_folder_id == None:
        m_folder = g_drive.CreateFile({'title': basename, 
                        'mimeType': 'application/vnd.google-apps.folder'})
    else:
        m_folder = g_drive.CreateFile({'title': basename, 
                        'mimeType': 'application/vnd.google-apps.folder',
                        'parents': [{'id': dest_folder_id}]})
    m_folder.Upload()

    files = glob.glob(folder_name+'/*')
    files.sort()
    m_files = []
    m_folders = []
    for it in files:
        if os.path.isdir(it):
            m_folders.append(it)
        else:
            m_files.append(it)

    for it in m_files:
        upload_file(g_drive, m_folder['id'], it)
    for it in m_folders:
        upload_folder(g_drive, m_folder['id'], it)
    
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--download',
                                help='download [file ID] / [folder ID]')
    parser.add_argument('-u', '--upload',
                                help='upload [file] / [folder]')
    parser.add_argument('-r', '--recursive',
                                help='download / upload recursively for folders',
                                action='store_true')
    parser.add_argument('-dest', '--destination',
                                help='download: destination folder; upload: destination folder ID')
    args = parser.parse_args()
    
    #Login to Google Drive and create drive object
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    g_drive = GoogleDrive(g_login)


    if args.recursive:
        if args.download != None:
            download_folder(g_drive, args.destination, args.download)
            pass
        if args.upload != None:
            upload_folder(g_drive, args.destination, args.upload)
            pass
        pass
    else:
        if args.download != None:
            download_file(g_drive, args.destination, args.download)
            pass
        if args.upload != None:
            upload_file(g_drive, args.destination, args.upload)
            pass
        pass

    pass
