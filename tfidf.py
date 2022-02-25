from parse import * 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(corpus)
names = vectorizer.get_feature_names()
data = vectors.todense().tolist()

# Create a dataframe with the results
df = pd.DataFrame(data, columns=names)


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
st = set(stopwords.words('english'))
#remove all columns containing a stop word from the resultant dataframe. 
df = df[filter(lambda x: x not in list(st) , df.columns)]
df.index = chapters

N = 5;
keywords = [list(i[1].sort_values(ascending=False)[:N].index.values) for i in df.iterrows()]