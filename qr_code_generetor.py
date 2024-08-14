import pyqrcode
import os
import time

print('Generate your QR code')

brute_url = input('Insert the URL: ')
url_processed = brute_url.replace('www.', '').replace(
    'https://', '').replace('http://', '')

url_domain = url_processed.split('/')[0]
url_name = url_domain.split('.')[0]

print('\nGenerating...')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

qr_created = pyqrcode.create(brute_url)

print('QR Code generated successfully!\n')
print('(Select the format you want to save it)\n')

formats = {
    'svg': 'Formato que ocupa menos espaço',
    'png': 'Formato com melhor qualidade de imagem',
    'text': 'Formato em texto ASCII',
}

for name, description in formats.items():
    print(name, description, sep=": ")

while True:
    selected_format = input('\nFile format: ').lower()

    if selected_format in formats:
        break

    print('Invalid Format')

# Criar a pasta 'qr_codes' se não existir
folder_name = 'qr_codes'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

new_file_name = f'qr_code_{url_name}.{selected_format}'
save_file = os.path.join(folder_name, new_file_name)

if selected_format == 'svg':
    qr_created.svg(
        file=save_file,
        scale=8,
    )
elif selected_format == 'png':
    qr_created.png(
        file=save_file,
        scale=8,
    )
elif selected_format == 'text':
    with open(save_file, 'w') as f:
        f.write(qr_created.text())

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

print('Generated Successfully!')
print(f'File saved at: {save_file}')
