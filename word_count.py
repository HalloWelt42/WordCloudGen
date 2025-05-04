import re
from collections import Counter


class WordCounter:

    def __init__(self, file, stopword_file='stopwords.txt', min_word_len=2, use_stopwords=True):
        self.__file = file
        self.__min_word_len = min_word_len
        self.__use_stopwords = use_stopwords
        self.__stopword_file = stopword_file
        if self.__use_stopwords:
            self.__stop_words = self.__load_stopwords()
        else:
            self.__stop_words = set()

    def __load_stopwords(self):
        with open(self.__stopword_file) as file:
            stopwords = set()
            for line in file:
                stopwords.add(line.strip().lower())
        return stopwords

    def __iterator_textfile(self):
        with (open(self.__file) as file):
            for line in file:
                words = line.split()
                # Entfernen von Satzzeichen und Umwandeln in Kleinbuchstaben
                for word in words:
                    # Entfernen von Satzzeichen und Umwandeln in Kleinbuchstaben
                    word = re.sub(r'[^\w\s]', '', word).lower()
                    if not word or len(word) < self.__min_word_len:
                        continue

                    if self.__use_stopwords and word in self.__stop_words:
                        continue

                    yield word

    def most_common_words(self, list_length=0):
        self.__iterator_textfile()

        # Zähle die Wörter
        words = []
        for word in self.__iterator_textfile():
            words.append(word)

        # Zähle die Häufigkeit der Wörter
        word_counts = Counter(words)

        # Sortiere die Wörter nach Häufigkeit
        if list_length > 0:
            word_counts = word_counts.most_common(list_length)
        else:
            word_counts = word_counts.most_common()

        return word_counts


def main():
    word_counter = WordCounter(file="beitrag.txt")

    # Ausgabe der häufigsten Wörter
    for word, count in word_counter.most_common_words(5):
        print(f'{word}: {count}')


if __name__ == '__main__':
    main()
