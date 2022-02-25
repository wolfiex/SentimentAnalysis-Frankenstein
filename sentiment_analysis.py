from operator import index
from parse import * 
from tfidf import keywords

# !pip install text2emotion
# !pip install textblob
from textblob import TextBlob
import text2emotion as te
from p_tqdm import p_map
import pandas as pd
# import nltk,tqdm
# nltk.download('omw-1.4')


'''
Emotion Classification
'''
print('Calculating Emotion Properties...')
emotion = p_map(te.get_emotion,corpus)
print(emotion)

df = pd.DataFrame(emotion,index=chapters)

'''
Emotion * Number of Words
'''
dfscale = df.copy()
nwords = [len(re.split(r'[\W\s]+',text)) for text in corpus]
for k in te.get_emotion('').keys():
    dfscale[k] = dfscale[k]*nwords



'''
TextBlob Sentiment Analysis
'''

print('Calculating Sentiment Properties...')
blob = p_map(TextBlob,corpus)

polarity = pd.DataFrame(p_map(lambda x: x.polarity,blob), index=chapters)
sentiment = pd.DataFrame(p_map(lambda x: x.subjectivity,blob), index=chapters)
polarity['keywords'] = keywords
sentiment['keywords'] = keywords


'''
What words are responsible for each ranking?
'''

def at(q):
    ''' Make a dataframe of the scores for each chapter '''
    e = pd.DataFrame(q.sentiment_assessments.assessments)
    e.index = [w[0] for w in e[0]]
    e.drop(0,axis=1,inplace=True)
    e.drop(3,axis=1,inplace=True)
    e.columns = ['polarity','subjectivity']
    return e

assesments = [at(d) for d in blob]


blob[1].noun_phrase