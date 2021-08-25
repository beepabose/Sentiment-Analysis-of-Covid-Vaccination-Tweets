import glob
import pandas as pd
files=glob.glob('./TEMP/*' )
D=pd.DataFrame()
L=[]
def Func(x):
    temp = pd.read_csv(x)
    return temp
L=list(map(Func,files))
result = pd.concat(L)
result.reset_index(inplace=True)
result=result[['created', 'followers', 'is_user_verified', 'location', 'name', 'retweets', 'text']]


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re
from nltk.stem import WordNetLemmatizer


stop_words=stopwords.words('english')
wnl = WordNetLemmatizer()


X=result['text']
cleaned_data=[]
for i in range(len(X)):
    y=re.sub(r"http\S+", "",X.iloc[i]) #URL
    y=re.sub(r"@\S+", "",y) #@rem
    y=re.sub('[^a-zA-Z]',' ',y)
    y=y.lower().split()
    y=[wnl.lemmatize(word) for word in y if (word not in stop_words)]
    y=' '.join(y)
    cleaned_data.append(y)
    
data2= pd.DataFrame(cleaned_data)
result['text_proc']=data2
Y=result['text_proc']

import  text2emotion as te
f=[]
for i in Y:
    f.append((te.get_emotion(i)))
	
    
new = pd.DataFrame.from_dict(f)
new['text_proc']=result['text_proc']
new['text']=result['text']
new['retweets']=result['retweets']
new['location']=result['location']
new['created']=result['created']
new['followers']=result['followers']
new['name']=result['name']
new['is_user_verified']=result['is_user_verified']




#country mapping

countries=pd.read_csv('worldcities.csv',header=0, sep=",")
result['country']='Not Available'
for i,n in result.iterrows():
    for j,c in countries.iterrows():
         if((c.country.lower() in str(n.location).lower()) & (n.country=='Not Available') & (n.location!='N/A')):
              result['country'].iloc[i]=c.country.title()
              break
         elif ((str(c.state).lower() in str(n.location).lower()) & (n.country=='Not Available') & (n.location!='N/A')):
              result['country'].iloc[i]=c.country.title()
              break
         elif ((str(c.city_ascii).lower() in str(n.location).lower()) & (n.country=='Not Available') & (n.location!='N/A')):
              result['country'].iloc[i]=c.country.title()
              break


