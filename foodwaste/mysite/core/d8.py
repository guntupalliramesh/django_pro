import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from textblob import TextBlob

inputText = ("Pthon is an Interpted, High-level,general-purpose programming"+"language. The NLTK module is a python package for Natural Language"+"Processing. TextBlob is a Python Library for processing textual data.")
nltkWordTokensize = word_tokenize(inputText)
print("\nWord Tokenization using NLTK\n",nltkWordTokensize)

nltkSentTOkenSize = sent_tokenize(inputText)
print("\nSent Tokenization using NLTK\n",nltkSentTOkenSize)

textblob_obj = TextBlob(inputText)
textblobwordTokenSize = textblob_obj.words
print("\nWord Tokenization using Textblob\n",textblobwordTokenSize)

textblobSentTokenSize = textblob_obj.sentences
print("\nSent Tokenization using TextBlob\n",textblobSentTokenSize)

