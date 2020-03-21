# Installation Guide

The Test-Edits is created in a Python Virtual Environment in Ubuntu (18.04) LTS, but is capable on running in any platform.

Python Version = 3.6.9

Steps on how to create a virtual environment.

```bash
# to install python virtualenv package
$> sudo python3 pip install virtualenv
# create a folder where you want to make virtualenv
$> mkdir project
$> cd project
$> python3 -m virtualenv venv
# takes some time and created a virtualenv, to check do dir, or ls -la
# activate the virtualenv
$> source venv/bin/activate
# you'll get a (venv) before your terminal address
#this will install all the necessary packages for you
(venv)$> pip install jupyterlab spacy pandas numpy scipy seaborn 
#this these are the pre-trained word embeddings that I'm going to use.
(venv)$> python -m spacy download en_core_web_md
# this one is spanish
(venv)$> python -m spacy download es_core_news_md
#after this you can clone the repository by doing
(venv)$>git clone https://github.com/srbhr/Test-Edits
(venv)$> cd Test-Edits
#this will start your jupyter lab environment
(venv)$> jupyter lab
#then click on the provided Notebooks to start with.
```

For further information you can refer to :

https://realpython.com/python-virtual-environments-a-primer/

https://www.geeksforgeeks.org/python-virtual-environment/

Packages used:

- spacy
- numpy
- pandas
- seaborn, matplotlib
- spacy en_core_web_md
- spacy es_core_news_md

