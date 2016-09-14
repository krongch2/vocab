import random

with open('vocab.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    chunks = text.split('\n\n')

n = len(chunks)
print(n)

while True:
    print('\n')
    random_idx = random.randint(0, n - 1)
    chunk = chunks[random_idx]
    for line in chunk.split('\n'):
        if line.startswith('-'):
            print(line)
    input()
    for line in chunk.split('\n'):
        if not line.startswith('-'):
            print(line)
    input()
