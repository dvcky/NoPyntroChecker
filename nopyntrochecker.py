import datetime
import hashlib
import os
import pathlib
import requests
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

def checkDatabase():
    if os.path.isdir('nopyntrochecker-db'):
        if os.path.isfile('nopyntrochecker-db.timestamp') and open('nopyntrochecker-db.timestamp', 'r').read() == str(datetime.date.today()):
            print('Local and up-to-date copy of the No-Intro database found!')
        else:
            print('Local copy of the No-Intro database found, but it is not up-to-date or missing a timestamp file!')
            option = input('Update database? (anything except y will be considered no) ')
            if option == 'y':
                updateDatabase()
    else:
            print('No local copy of No-Intro\'s database found!')
            updateDatabase()

def updateDatabase():
    print('--------------------------------')
    if os.path.isdir('nopyntrochecker-db'):
        print('Removing old database...')
        shutil.rmtree('nopyntrochecker-db')
        print('Removed old database!')
    session = requests.Session()
    session.get('https://datomatic.no-intro.org/index.php?page=download&op=daily')
    page = session.post('https://datomatic.no-intro.org/index.php?page=download&op=daily', {'dat-type': 'standard', 'prepare_2': 'Prepare'})
    print('Session requested with ID ' + page.url.split('d=',1)[1])
    print('Downloading database file...')
    shutil.copyfileobj(session.post(page.url, {'download': 'Download'}, stream=True).raw, open('nopyntrochecker-db.zip', 'wb'))
    print('Downloaded database file.')
    print('Extracting database file...')
    zipfile.ZipFile('nopyntrochecker-db.zip').extractall('nopyntrochecker-db')
    print('Extracted database file.')
    print('Cleaning up...')
    os.remove('nopyntrochecker-db.zip')
    timestamp = open('nopyntrochecker-db.timestamp', 'w').write(str(datetime.date.today()))
    print('Created timestamp file. (' + str(datetime.date.today()) + ')')

def scanFile(file):
    print('--------------------------------')
    print('File: '+file)
    print('Hashing file...', end='\r')
    md5 = hashlib.md5(open(file, 'rb').read()).hexdigest().upper()
    print('Hash generated: ' + md5)
    print('--------------------------------')
    print('Scanning the No-Intro database...')
    database = next(os.walk('nopyntrochecker-db'))[2]  
    for platform in database:
        print('Scanning: ' + platform.split('(', 1)[0] + '                                ', end='\r')
        tree = ET.ElementTree(ET.fromstring(open('nopyntrochecker-db/' + platform, 'r').read().replace('&','&amp;')))
        root = tree.getroot()
        for game in root:
            for scan in game:
                if scan.get('md5') == md5:
                    name = game.get('name', default=None).replace('&amp;','&')
                    print('Found in ' + platform.split('(', 1)[0] + '                                ')
                    print('--------------------------------')
                    print('Game: ' + name)
                    print()
                    return [md5, name]
    print('Scan finished.                                ')
    print('--------------------------------')
    print('No matches found.')
    print()
    return [md5, 'Failed']

def scanFolder(folder):
    log = open('nopyntrochecker-logs/nopyntrochecker-' + str(datetime.datetime.now()).replace(':','').replace('.','') + '.log', 'a')
    log.write('Check started at ' + str(datetime.datetime.now()) + '.')
    folderpath = folder
    folder = next(os.walk(folder))[2]
    for file in folder:
        file = folderpath + '/' + file
        log.write('\n\nFile: ' + file)
        scan = scanFile(file)
        log.write('\nMD5: ' + scan[0])
        log.write('\nCheck: ' + scan[1])
        log.write('\nTime: ' + str(datetime.datetime.now()))
    log.write('\n\nCheck finished at ' + str(datetime.datetime.now()) + '.')

#INIT CODE
print('--------------------------------')
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet', 'requests'])
print('--------------------------------')
if len(sys.argv) != 2:
    print()
    print('Invalid usage!')
    print('Please use this script in a terminal with one file or folder path as the argument!')
    print('(ex: py nopyntrochecker.py /path/to/file/filename.filetype OR py nopyntrochecker.py /path/to/folder/foldername/)')
else:
    arg = str(sys.argv[1])
    if not os.path.isdir('nopyntrochecker-logs'):
            os.mkdir('nopyntrochecker-logs')
    print()
    if os.path.isfile(arg):
        print('FILE SCAN')
        checkDatabase()
        log = open('nopyntrochecker-logs/nopyntrochecker-' + str(datetime.datetime.now()).replace(':','').replace('.','') + '.log', 'a')
        log.write('Check started at ' + str(datetime.datetime.now()) + '.')
        scan = scanFile(arg)
        log.write('\nMD5: ' + scan[0])
        log.write('\nCheck: ' + scan[1])
        log.write('\nTime: ' + str(datetime.datetime.now()))
        log.write('\n\nCheck finished at ' + str(datetime.datetime.now()) + '.')
    else:
        if os.path.isdir(arg):
            print('FOLDER SCAN')
            checkDatabase()
            scanFolder(arg)
        else:
            print('--------------------------------')
            print('Invalid usage!')
            print('File or folder does not exist! Make sure the path was entered properly!')

#EXIT CODE
print('--------------------------------')
input('Press enter to continue...')
print()
