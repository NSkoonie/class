exclude = ('.', ',', '\"', '!', '?')

try:
    with open('wordFrequency.txt', 'r') as f:
        dataRaw = f.readlines()
        
except FileNotFoundError:
    print('wordFrequency.txt not found.')

else:
    dataFine = [d.strip() for d in dataRaw]
    pWords = ' '.join(dataFine).split(' ')   #join lines then separate all words by spaces
    words = []                      #create an empty list
    for word in pWords:
        s = ''.join(ch for ch in word if ch not in exclude)
        if s != '':
            words.append(s.lower())

    dataDic = {}
    for word in words:
        c = 0
        for i in range(len(words)):
            if words[i] == word:
                c += 1
                dataDic[word] = c

    for key in dataDic:
        print('{:10}{:6}'.format(key, dataDic[key]))
