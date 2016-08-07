import re
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet

#Initialziing the Regular expression patterns to replace words like 'can't' with 'cannot'
replacement_patterns =[
    (r'won\'t','will not'),
    (r'can\'t','cannot'),
    (r'i\'m','i am'),
    (r'(\w+)\'ll','\g<1> will'),
    (r'(\w+)\'ve','\g<1> have'),
    (r'(\w+)\'s','\g<1> is'),
    (r'(\w+)\'re','\g<1> are'),
    (r'(\w+)\'d','\g<1> would')

]
patterns = [(re.compile(regex),repl) for (regex,repl) in replacement_patterns]

#Function to replace the words like  "can't" with 'cannot'
def replace(text):
    s = text
    for (pattern,repl) in patterns:
        s = re.sub(pattern,repl,s)
    return s


'''
Class to replace words with repeated characters like 'niceeee','loooove' with 'nice','love'
This class uses wordnet to prevent replacing the correct words. Ex: The word 'cool' is a dictionary word.
It should not be replaced as 'col'
'''
class RepeatReplacer:
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'


    def replace(self,word):
        if wordnet.synsets(word):
            return word
        replaced = self.repeat_regexp.sub(self.repl,word)

        if replaced != word:
            return self.replace(replaced)
        else:
            return replaced

#Main function
def clean(text):

    sent_tokenizer = PunktSentenceTokenizer()
    tokenized = sent_tokenizer.tokenize(text)
    replacer = RepeatReplacer()
    tagged =[]

    try:
        for sent in tokenized:
            s = replace(sent)
            words = nltk.word_tokenize(s)
            for i,word in enumerate(words):
                words[i]=replacer.replace(word)
            tagged.append(nltk.pos_tag(words))

    except Exception as e:
        print(str(e))

    return tagged

