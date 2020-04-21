# Requirements
sudo pip2 install pydrive
sudo pip2 install httplib2==0.15.0

# Activate Google Drive API
https://pythonhosted.org/PyDrive/quickstart.html

# Usage
gdrive.py [-h] [-d DOWNLOAD] [-u UPLOAD] [-r] [-dest DESTINATION]

optional arguments:
  -h, --help            show this help message and exit
  -d DOWNLOAD, --download DOWNLOAD
                        download [file ID] / [folder ID]
  -u UPLOAD, --upload UPLOAD
                        upload [file] / [folder]
  -r, --recursive       download / upload recursively for folders
  -dest DESTINATION, --destination DESTINATION
                        download: destination folder; upload: destination
                        folder ID

Example:
<ul>
    <li> Upload a file: python gdrive -u file.txt [-d 1ABCDEFGHIJABCDEFGHIJABCDEFGHIJAB] </li>
    <li> Upload a folder: python gdrive -r -u abc/ [-d 1ABCDEFGHIJABCDEFGHIJABCDEFGHIJAB]  </li>
    <li> Download a file: python gdrive -d 1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB 
                                            [-d /home/xyz/abc] </li>
    <li> Download a folder: python gdrive -r -d 1XXXXXXXXXXXXXXXXXXXXXXXXXXXXABCB 
                                            [-d /home/xyz/abc] </li>                                            
</ul>