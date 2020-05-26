import datetime
import hashlib
import os
import pathlib
import requests
import shutil
import sys
import xml.etree.ElementTree as ET
import zipfile

def scan():
    print('--------------------------------\nFile: '+file)
    print('Hashing file...', end='\r')
    md5 = hashlib.md5(open(file, 'rb').read()).hexdigest().upper()
    print('Hash generated: ' + md5 + '\n--------------------------------\nScanning the No-Intro database...')
    files = next(os.walk('nopyntrochecker-db'))[2]  
    for platform in files:
        print('Scanning: ' + platform.split('(', 1)[0] + '                                ', end='\r')
        tree = ET.ElementTree(ET.fromstring(open('nopyntrochecker-db/' + platform, 'r').read().replace('&','&amp;')))
        root = tree.getroot()
        for game in root:
            for scans in game:
                if scans.get('md5') == md5:
                    print('Found in ' + platform.split('(', 1)[0] + '                                \n--------------------------------\nTitle: ' + game.get('name', default=None) + '\n--------------------------------')
                    return
    print('Scan finished.                                \n--------------------------------\nNo matches found :(\n--------------------------------')

def update():
    print('--------------------------------')
    if os.path.isdir('nopyntrochecker-db'):
        print('Removing old database...')
        shutil.rmtree('nopyntrochecker-db')
    session = requests.Session()
    session.get('https://datomatic.no-intro.org/index.php?page=download&op=daily')
    page = session.post('https://datomatic.no-intro.org/index.php?page=download&op=daily', {'dat-type': 'standard', 'prepare_2': 'Prepare'})
    print('Download session requested with ID ' + page.url.split('d=',1)[1])
    print('Downloading database...')
    shutil.copyfileobj(session.post(page.url, {'download': 'Download'}, stream=True).raw, open('nopyntrochecker-db.zip', 'wb'))
    print('Download complete.                                ')
    print('Extracting database file...')
    zipfile.ZipFile('nopyntrochecker-db.zip').extractall('nopyntrochecker-db')
    print('File extracted.                                ')
    print('Deleting database file...')
    os.remove('nopyntrochecker-db.zip')
    print('File deleted.                                ')
    timestamp = open('nopyntrochecker-timestamp', 'w')
    timestamp.write(str(datetime.date.today()))
    print('Created timestamp file. (' + str(datetime.date.today()) + ')')
    scan()


if len(sys.argv) != 2:
    print('\n--------------------------------\nInvalid usage!\nPlease use this script in a terminal with one filepath as the argument!\n(ex: py nopyntrochecker.py /path/to/file/filename.filetype)\n--------------------------------')
    input('Press enter to continue...')
    print()
    sys.exit()
else:
    file = str(sys.argv[1])
    if os.path.isfile(file):
        print('\n--------------------------------')
        if os.path.isdir('nopyntrochecker-db'):
            if os.path.isfile('nopyntrochecker-timestamp') and open('nopyntrochecker-timestamp', 'r').read() == str(datetime.date.today()):
                print('Local and up-to-date copy of No-Intro database found!')
                scan()
            else:
                option = input('Local copy of No-Intro database found, but not up-to-date! Update database? (anything except y will be considered no) ')
                if option == 'y':
                    update()
                else:
                    scan()
        else:
            print('No local copy of No-Intro\'s database found!')
            update()
        input('Press enter to continue...')
        print()
        sys.exit()
    else:
        print('\n--------------------------------\nInvalid usage!\nFile does not exist! Make sure the filepath was entered properly!\n--------------------------------')
        input('Press enter to continue...')
        print()
