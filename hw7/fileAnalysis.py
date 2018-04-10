exclude = ('.', ',', '\"', '!', '?')

def handleFile(file):
    try:
        with open(file, 'r') as f:
            data = f.readlines()

    except FileNotFoundError:
        print(file + 'not found.')

    else:
        data = [d.strip() for d in data]
        pWords = ' '.join(data).split(' ')

        words = set()
        for word in pWords:
            s = ''.join(ch for ch in word if ch not in exclude)
            if s != '':
                words.add(s.lower())

        return words

words1 = handleFile('file1.txt')
words2 = handleFile('file2.txt')

print('\nAll unique words contained in both files:')
print(words1 | words2)

print('\nWords common to both files:')
print(words1 & words2)

print('\nWords in file1 but not in file2:')
print(words1 - words2)

print('\nWords in file2 but not in file1:')
print(words2 - words1)

print('\nWords in file1 or file2, but not both:')
print(words1 ^ words2)
