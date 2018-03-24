from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import re
import zlib
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i",
                        "--input",
                        dest="input",
                        action="store",
                        default=None,
                        required=True,
                        help="Nama File")
args = arg_parser.parse_args()

#CRC

buffersize = 65536

with open('E:/an8/temp/temp.mkv', 'rb') as afile:
    buffr = afile.read(buffersize)
    crcvalue = 0
    while len(buffr) > 0:
        crcvalue = zlib.crc32(buffr, crcvalue)
        buffr = afile.read(buffersize)

crc=format(crcvalue & 0xFFFFFFFF, '08x')

#Rename

argument=args.input
argument_slash=re.sub('HorribleSubs','GarisMiring-an8',argument)
argument_slasher=argument_slash.replace('[480p]','[TV][480p-AAC]['+crc+']')
os.rename('E:/an8/temp/temp.mkv', 'E:/an8/temp/'+argument_slasher)
ukuran_beha=os.path.getsize('E:/an8/temp/'+argument_slasher)
maho=ukuran_beha/1024
kuy=maho/1024
xxx=re.compile(r"(\d*)\.\d*")
ukuran_cari=re.search(xxx,str(kuy))
ukuran_fix=ukuran_cari.group(1)

#Upload

DEFAULT_SETTINGS = {
'client_config_backend': 'file',
'client_config_file': 'client_secrets.json',    
'oauth_scope': ['https://www.googleapis.com/auth/drive']   
}

gauth = GoogleAuth()

drive = GoogleDrive(gauth)
file1 = drive.CreateFile({'title': argument_slasher})  
file1.SetContentFile('E:/an8/temp/'+argument_slasher) 
file1.Upload()    
               
file1.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})
link=file1['alternateLink']
regex_link=re.compile(r"/d/(.*)/")
slash_link=re.search(regex_link,link)
print(link)
print('')
print('Kode Google Drive = '+slash_link.group(1))

#Proses Posting

nomor = re.compile=(r"<td>(\d)</td>\s*.*\s*</td>\s*.*\s*</tr>\s*<!--Posting-->")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as nomorz:
    dataz = nomorz.read()
    nomorz.seek(0)
    fuck=re.search(nomor,dataz)
    pl0x=int(fuck.group(1))+1

html_str = """
 <tr kode="..""" + slash_link.group(1) +"""" class="">
            <td>""" +str(pl0x)+"""</td>
            <td class="name">""" + argument_slasher +"""
</td>
            <td class="size">"""+ ukuran_fix +"""</td>
        </tr>
    <!--Posting-->

"""

regex = re.compile=(r"<!--Posting-->")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as index:
    data = index.read()
    index.seek(0)
    index.write(re.sub(r"<!--Posting-->",html_str,data))
    index.truncate()
index.close()



