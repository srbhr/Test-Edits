class WordEmbeddings:
    
    try:
        import spacy
        engnlp = spacy.load('en_core_web_md')
        spanlp = spacy.load('es_core_news_md')
    except ImportError:
            print("Module Not Available")
    
    def __init__(self, text = "abcdefghijklmnopqrstuvwxyz"):
        self.text = text
        
    def get_spanish_vectors(self, remove_nulls=True):
        doc = spanlp(self.text)
        vector = []
        if remove_nulls == True:
            for token in doc:
                if token.has_vector == True:
                    vector.append([token.text, token.vector_norm])
        else:
            for token in doc:
                vector.append([token.text, token.vector_norm])
                
        return vector
    
    def get_english_vectors(self, remove_nulls=True):
        doc = engnlp(self.text)
        vector = []
        if remove_nulls == True:
            for token in doc.tokens:
                if token.has_vector == True:
                    vector.append([token.text, token.vector_norm])
        else:
            for token in doc.tokens:
                vector.append([token.text, token.vector_norm])
                
        return vector
        
        