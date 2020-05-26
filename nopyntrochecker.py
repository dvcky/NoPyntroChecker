import hashlib
import os.path
import pathlib
import requests
import sys

def filetype(name):
    list = {
        '.gb': 'Nintendo - Game Boy',
        '.gba': 'Nintendo - Game Boy Advance',
        '.gbc': 'Nintendo - Game Boy Color',
        '.nds': 'Nintendo - Nintendo DS',
        '.nes': 'Nintendo - Nintendo Entertainment System',
        '.md': 'Sega - Mega Drive - Genesis',
        '.sfc': 'Nintendo - Super Nintendo Entertainment System',
        '.v64': 'Nintendo - Nintendo 64',
        '.z64': 'Nintendo - Nintendo 64'
    }
    return list.get(name, "")

if len(sys.argv) != 2:
    print('\n--------------------------------\nInvalid usage!\nPlease use this script in a terminal with one filepath as the argument!\n(ex: py nopyntrochecker.py /path/to/file/filename.filetype)\n--------------------------------')
    input('Press enter to continue...')
    print()
    sys.exit()
else:
    file = str(sys.argv[1])
    if os.path.isfile(file):
        if filetype(pathlib.Path(file).suffix) == '':
            print('\n--------------------------------\nInvalid file type!\nMake sure your file ends in either nes, md, sfc, z64, v64, gb, gba, gbc, or nds!\n--------------------------------')
            input('Press enter to continue...')
            print()
            sys.exit()
        else: 
            print('\n--------------------------------\nFile selected!\n'+file+'\n--------------------------------\nHashing file...')
            md5 = hashlib.md5(open(file, 'rb').read()).hexdigest()
            print('Hash generated: ' + md5 + '\n--------------------------------\nScanning the No-Intro database...')

            data = {'sel_s': filetype(pathlib.Path(file).suffix), 'where': '2', 'stext': md5}
            url = 'https://datomatic.no-intro.org/index.php?page=search'

            session = requests.Session()
            session.get(url)
            post = str(session.post(url,data).content).replace('\\n','').replace('\\t','').split('/fieldset></div>',1)[1].split('</article',1)[0]
            if post.startswith('U'):
                print('Uh oh! It looks like your file\'s hash does not match with any on the No-Intro database!\n--------------------------------')
            else:
                print('Match found! Your game was identified as: ' + post.split('show_record',1)[1].split('>',1)[1].split('<',1)[0] + '\n--------------------------------')
            input('Press enter to continue...')
            print()
    else:
        print('\n--------------------------------\nInvalid usage!\nFile does not exist! Make sure the filepath was entered properly!\n--------------------------------')
        input('Press enter to continue...')
        print()
