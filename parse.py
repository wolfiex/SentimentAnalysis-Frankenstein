import re 
import json

text = open('novel.txt','r').read()
text = text.replace('.',' ')
text = re.sub(r'\s+',' ',re.sub(r'[^\w \s]','',text) ).lower()


corpus = re.split('chapter \d+',text)
chapters = ['Letters']
chapters.extend(re.findall('chapter \d+',text))