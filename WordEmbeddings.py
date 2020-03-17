class WordEmbeddings:

    import spacy
    spanlp = spacy.load('es_core_news_md')
    engnlp = spacy.load('en_core_web_md')

    def __init__(self, text="abcdefghijklmnopqrstuvwxyz"):
        self.text = text

    def get_spanish_vectors(self, remove_nulls=True, normalized=True):

        doc = self.spanlp(self.text)
        vector = []
        if remove_nulls == True:
            for token in doc:
                if token.has_vector == True:
                    if normalized == True:
                        vector.append([token.text, token.vector_norm])
                    else:
                        vector.append([token.text, token.vector])

        else:
            for token in doc:
                vector.append([token.text, token.vector_norm])

        return vector

    def get_english_vectors(self, remove_nulls=True, normalized=True):

        doc = self.engnlp(self.text)
        vector = []
        if remove_nulls == True:
            for token in doc.tokens:
                if token.has_vector == True:
                    if normalized == True:
                        vector.append([token.text, token.vector_norm])
                    else:
                        vector.append([token.text, token.vector])
        else:
            for token in doc.tokens:
                vector.append([token.text, token.vector_norm])

        return vector

# ++++++++++++++++MAIN+++++++++++++++++++


# word = WordEmbeddings(text='Gracias').get_spanish_vectors()
# print(word)
