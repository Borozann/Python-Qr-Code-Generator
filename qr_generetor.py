import pyqrcode as qr
import os
import time

print('Generate your qr code')

brute_url = input(('Insert the url: '))
url_processed = brute_url.replace('www.', '').replace(
    'https://', '').replace('http://', '')

url_domain = url_processed.split('/')[0]

url_name = url_domain.split('.')[0]

print('\n')
print('Generating...')
time.sleep(1)
os.system('cls')

qr_created = qr.create(brute_url)

print('Qr Code generated sucessfull!\n')
print('(Select the format you want to save it)\n')

formats = {
    'svg': 'ocupa menos espaco',
    'png': 'melhor qualidade de foto',
    'jpeg': 'etc',
    'jpg': 'etc'
}


for name, description in formats.items():
    print(name, description, sep=": ")

while True:
    selected_format = input('\nFile format: ')

    if selected_format in formats:
        break

    print('Inválid Format')

new_file_name = f'qr_code_{url_name}.{selected_format}'
print(new_file_name)
