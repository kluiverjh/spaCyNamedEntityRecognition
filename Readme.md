



## Named Entity Recognition (NER) example for spaCy

Small demo application how to extract NER with spaCy. 



It is based on this article https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy

The example can run in python or be compiled to a single .exe (with pyinstaller ). This example uses python 3.7, because the spaCy packages are precompiled for this version (for later version you have to compile spaCy youyself).

## Setup environment

```
// Create python virtual environment (only once)
python -m venv .env
// Activate environment
.env\Scripts\activate
//
pip install -U spacy
// Download models (https://spacy.io/models/en)
python -m spacy download en_core_web_sm
// Install PyInstaller (only needed when you need to create .exe)
```

## Create executable from python code (optional)

```
// Build executable
pyinstaller -F main.spec
```

## Test application

```
// The application will pass plaintext.txt to spaCy and then output NER
python main.py
// Run executable
copy planintext.txt ./dist/
cd ./dist/
main.exe
```
## Websites

[spaCy website](https://spacy.io/)

[spaCy NER categories](https://spacy.io/api/annotation#named-entities)

[PyInstaller Quickstart — PyInstaller bundles Python applications](https://www.pyinstaller.org/)

