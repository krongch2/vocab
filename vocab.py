import random

with open('vocab.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    chunks = text.split('\n\n')

# for chunk in chunks:
    # print(chunk.encode('utf-8'))
    # print(chunk)
n = len(chunks)
random_idx = random.randint(0, n - 1)
print(n)
for i in range(1):
    print(chunks[random_idx + i] + '\n')
