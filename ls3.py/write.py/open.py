import re

with open('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    print('Символов в тексе -',len(content))
    print('Кол-во слов в текстты а - ', len(content.split()))


with open('referat.txt', 'r+',encoding='utf-8') as referat_2:
    content_referat_2 = referat_2.read()
    print(re.sub('[^i]', '.', content_referat_2))
