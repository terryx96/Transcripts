from docx import Document
from nltk import Text, word_tokenize
def wordToTxt(source, destination):
    document = Document(source)
    txtFile = open(destination, "w+")
    for para in document.paragraphs:
        txtFile.write("{}\n".format(para.text))

def txtToNltk(text):
    tokens = word_tokenize(text)
    return Text(tokens)
