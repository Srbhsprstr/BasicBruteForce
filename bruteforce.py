import zipfile
from tqdm import tqdm
charlist = 'abcdefghijklmnopqrstuvwxyz0123456789'
complete = []

for current in range(6):
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a

z = zipfile.ZipFile('document.zip')
for passw in tqdm(complete,desc="checking password"):
    try:
        z.setpassword(passw.encode('ascii'))
        z.extract('document.txt')
        print(f'password is {passw}')
        break
    except:
        pass
