import string

zeros_list = [0 for _ in range(26)]
counts = {char: num for char, num in zip(string.ascii_lowercase, zeros_list)}

with open('words.txt', 'r') as f:
    for line in f:
        for alpha in string.ascii_lowercase:
            counts[alpha] += line.count(alpha)

for key, value in counts.items():
    print(f'{key}: {value:,}')

total_chars = sum(counts.values())

print('\n\n')

for key, value in counts.items():
    percent_val = (value/total_chars)*100
    print(f'{key}: {percent_val:.2f} %')
