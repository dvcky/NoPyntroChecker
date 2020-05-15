import hashlib
import requests

print('--------------------------------\nSelect a game file to check...')
file = input('File chosen (put filepath here): ')
print('\n--------------------------------\nHashing file...')

md5 = hashlib.md5(open(file, 'rb').read()).hexdigest()
print('Hash generated: ' + md5 + '\n--------------------------------\nScanning No-Intro database for any available matches...')

data = {'stext': md5, 'where': '2'}
url = 'https://datomatic.no-intro.org/index.php?page=search'

post = str(requests.post(url,data).content).replace('\\n','').replace('\\t','').split('/fieldset></div>',1)[1].split('</article',1)[0]
if post.startswith('U'):
    print('Uh oh! It looks like you either input an invalid game file, or the game has been tampered with!\n--------------------------------\nPress enter to continue...')
else:
    print('Match found! Your game was identified as: ' + post.split('show_record',1)[1].split('>',1)[1].split('<',1)[0] + '\n--------------------------------\nPress enter to continue...')
input('')
