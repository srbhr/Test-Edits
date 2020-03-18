class WordEmbeddings:

    try:
        import spacy
        spanlp = spacy.load('es_core_news_md')
        engnlp = spacy.load('en_core_web_md')
    except ImportError:
        print('Module not Found spacy, intall it with pip install spacy')

    def __init__(self, text="abcdefghijklmnopqrstuvwxyz"):
        self.text = text

    """
        Gets the WordEmbeddings from the Spacy's in module included Glove Vectors for Spanish Language, these have
        the Dimensions upto 50.(Spanish)(Medium Data)
    """

    def get_spanish_vectors(self, normalized=True, remove_text=False):
        """
            The remove_text parameter removes the Word Text, if you don't want any additional 
            text data along with the coresponding vectors.
            Normalized = True returns a Prime Component based on t-SNE/PCA/LDA from the Spacy's Vectors.
            Normalized = False returns the whole 50 Dimensional Data.
        """

        doc = self.spanlp(self.text)
        vector = []
        if remove_text == False:
            for token in doc:
                if token.has_vector == True:
                    if normalized == True:
                        vector.append([token.text, token.vector_norm])
                    else:
                        vector.append([token.text, token.vector])
        else:
            for token in doc:
                if token.has_vector == True:
                    if normalized == True:
                        vector.append(token.vector_norm)
                    else:
                        vector.append(token.vector)

        return vector

    """
        Gets the WordEmbeddings from the Spacy's in module included Glove Vectors, these have
        the Dimensions upto 300.(English)(Medium Data)
    """

    def get_english_vectors(self, remove_text=False, normalized=True):
        """
            The remove_text parameter removes the Word Text, if you don't want any additional 
            text data along with the coresponding vectors.
            Normalized = True returns a Prime Component based on t-SNE/PCA/LDA from the Spacy's Vectors.
            Normalized = False returns the whole 300 Dimensional Data.
        """

        doc = self.engnlp(self.text)
        vector = []
        if remove_text == False:
            for token in doc.tokens:
                if token.has_vector == True:
                    if normalized == True:
                        vector.append([token.text, token.vector_norm])
                    else:
                        vector.append([token.text, token.vector])
        else:
            for token in doc:
                if token.has_vector == True:
                    if normalized == True:
                        vector.append(token.vector_norm)
                    else:
                        vector.append(token.vector)

        return vector

# ++++++++++++++++MAIN+++++++++++++++++++


# word = WordEmbeddings(text='Gracias').get_spanish_vectors()
# print(word)
