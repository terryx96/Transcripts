import nltk
import docx
from docx import Document
import lxml
# from nltk.book import *
from wordConversion import *

wordToTxt("crypto.docx", "output.txt")
file = open("./output.txt", "r")
text = file.readlines()

tokens = nltk.word_tokenize(" ".join(text))
nltkText = nltk.Text(tokens)

nltkText.concordance("algorithm")



file.close()



