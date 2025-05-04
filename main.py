from wordcloud import WordCloud, STOPWORDS

def main():
    with open('beitrag.txt') as file:
        text = file.read()

    wordcloud = WordCloud(width=1920, height=1080)

    with open('stopwords.txt') as file:
        for word in file:
            word = word.strip()
            if word:
                STOPWORDS.add(word)

    wordcloud.generate(text)
    wordcloud.to_file('wordcloud.png')


if __name__ == '__main__':
    main()
