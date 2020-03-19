# Test-Edits

#### Visualizing the Machine Translated and Post-Edited Sentences using the Respective Word Vector(Normalized).

This Repository contains the Apertium Machine Translated Sentences, and the Google, Microsoft, Yandex Machine Translated Sentences for English-Spanish Pair. Along with that, it also contains the Human Post-Edited sentences, as improvements for the MT tool.

The code in the Jupyter Notebooks: **Apertium_Test-Edits.ipynb** tries best to represent the difference between the Machine Translated and the Post-Edited sentences. **Google_Test-Edits.ipynb** is a measure to show the same. 

The Analysis of each is done in the respective Notebooks.

The JSON Data is in the Data Folder.

### Approach

At first the sentences were converted into Word Embeddings (for each word) using spaCy's built in Word2Vector Algorithm (that uses Glove Vectors) and then it was normalized using the `vector_norm`

method which either uses t-SNE or LDA for normalization of High Dimension Data.

This was then plotted against each other to represent the difference in translations.

#### Why Have I chosen to visualize data instead of just showing the accuracy measures?

The approach will take the same measure, instead of using spacy's normalized vector rather I'll use the whole 50 Dimensional data to compute an appropriate distance to get the word difference.

### Requirements 🛠

spacy (and english, spanish data)

pandas

matplotlib

seaborn

numpy 



