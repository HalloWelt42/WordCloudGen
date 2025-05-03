def mein():
    with open('stopwords.txt') as file:
        stopwords = set()
        for line in file:
            stopwords.add(line.strip().lower())

    word_count = {}
    with open('beitrag.txt') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?()[]{}"\'')
                if word:
                    word = word.lower()
                    # Überprüfen, ob das Wort ein Stopwort ist
                    if word in stopwords:
                        continue
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    # sortieren nach häufigkeit der wörter aus word_count
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    for word, count in sorted_word_count:
        print(f"{word}: {count}")

if __name__ == '__main__':
    mein()
