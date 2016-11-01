import random

with open('vocab.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    chunks = text.split('\n\n')

n = len(chunks)
print(n)
last_nwords = 20
deck = chunks[-last_nwords:]
while True:
    print('\n')
    card = random.choice(deck)
    for line in card.split('\n'):
        if line.startswith('-'):
            print(line, end='')
    input()
    for line in card.split('\n'):
        if not line.startswith('-'):
            print(line)
    input()
