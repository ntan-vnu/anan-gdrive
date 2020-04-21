# Requirements
sudo pip2 install pydrive               <br>
sudo pip2 install httplib2==0.17.0      <br>

# Activate Google Drive API
<ol class="arabic simple">
<li>Go to <a class="reference external" href="https://console.developers.google.com/iam-admin/projects">APIs Console</a> and make your own project.</li>
<li>Search for ‘Google Drive API’, select the entry, and click ‘Enable’.</li>
<li>Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.</li>
<li>Now, the product name and consent screen need to be set -&gt; click ‘Configure consent screen’ and follow the instructions. Once finished:</li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li>Select ‘Application type’ to be <em>Web application</em>.</li>
<li>Enter an appropriate name.</li>
<li>Input <em>http://localhost:8080</em> for ‘Authorized JavaScript origins’.</li>
<li>Input <em>http://localhost:8080/</em> for ‘Authorized redirect URIs’.</li>
<li>Click ‘Save’.</li>
</ol>
</div></blockquote>
<ol class="arabic simple" start="5">
<li>Click ‘Download JSON’ on the right side of Client ID to download <strong>client_secret_&lt;really long ID&gt;.json</strong>.</li>
</ol>
<p>The downloaded file has all authentication information of your application.
<strong>Rename the file to “client_secrets.json” and place it in your working directory.</strong></p>

Read more: https://pythonhosted.org/PyDrive/quickstart.html

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