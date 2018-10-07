with open('referat.txt', 'r', encoding='utf-8') as f1:
    content = f1.read()
    print(len(content))
    sum_word = 0

with open('referat.txt', 'r', encoding='utf-8') as f2:
    for line in f2:
        sum_word += len(line.split(' '))
        print(line.split(' '))
        print(sum_word)

new_content = content.replace('.', '!')
with open('referat3.txt', 'w', encoding='utf-8') as f3:
    f3.write(new_content)