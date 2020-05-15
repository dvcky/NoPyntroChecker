import hashlib
import requests
import tkinter
import tkinter.filedialog

print('--------------------------------\nSelect a game file to check...')
tkinter.Tk().withdraw()
file = tkinter.filedialog.askopenfilename()
print('File chosen: ' + file + '\n--------------------------------\nHashing file...')

md5 = hashlib.md5(open(file, 'rb').read()).hexdigest()
print('Hash generated: ' + md5 + '\n--------------------------------')

data = {'stext': md5, 'where': '2'}
url = 'https://datomatic.no-intro.org/index.php?page=search'
print('Scanning No-Intro database for any available matches...')

post = str(requests.post(url,data).content).replace('\\n','').replace('\\t','').split('/fieldset></div>',1)[1].split('</article',1)[0]
if post.startswith('U'):
    print('Uh oh! It looks like you either input an invalid game file, or the game has been tampered with!')
else:
    print('Match found! Your game was identified as: ' + post.split('show_record',1)[1].split('>',1)[1].split('<',1)[0] + '\n--------------------------------\nPress enter to continue...')
input('')
