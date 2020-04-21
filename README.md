# Requirements
sudo pip2 install pydrive               <br>
sudo pip2 install httplib2==0.15.0      <br>

# Activate Google Drive API
https://pythonhosted.org/PyDrive/quickstart.html

# Usage
<pre>
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
</pre>
Example:
<ul>
    <li> Upload a file: python gdrive -u file.txt <i>[-d 1ABCDEFGHIJABCDEFGHIJABCDEFGHIJAB]</i> </li>
    <li> Upload a folder: python gdrive -r -u abc/ <i>[-d 1ABCDEFGHIJABCDEFGHIJABCDEFGHIJAB]</i>  </li>
    <li> Download a file: python gdrive -d 1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB <i>[-d /home/xyz/abc]</i> </li>
    <li> Download a folder: python gdrive -r -d 1XXXXXXXXXXXXXXXXXXXXXXXXXXXXABCB <i>[-d /home/xyz/abc]</i>  </li>                                            
</ul>