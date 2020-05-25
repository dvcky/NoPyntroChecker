import hashlib
import os.path
import requests
import sys

if len(sys.argv) != 2:
    print('\n--------------------------------\nInvalid usage!\nPlease use this script in a terminal with one filepath as the argument!\n(ex: py nopyntrochecker.py /path/to/file/filename.filetype)\n--------------------------------')
    input('Press enter to continue...')
    print()
    sys.exit()
else:
    file = str(sys.argv[1])
    if os.path.isfile(file):
        print('\n--------------------------------\nFile selected!\n'+file+'\n--------------------------------\nHashing file...')
        md5 = hashlib.md5(open(file, 'rb').read()).hexdigest()
        print('Hash generated: ' + md5 + '\n--------------------------------\nScanning No-Intro database for any available matches...')

        data = {'stext': md5, 'where': '2'}
        url = 'https://datomatic.no-intro.org/index.php?page=search'

        post = str(requests.post(url,data).content).replace('\\n','').replace('\\t','').split('/fieldset></div>',1)[1].split('</article',1)[0]
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
