import pandas as pd 
from urllib.parse import * 
import tldextract
import re
from urlexpander import *
dataset=pd.read_csv("D:\\projects\\url_july1.csv")
ds=dataset.copy()





urls=ds.iloc[:,0]
result=ds.iloc[:,1]
df=[]
col=['dots_url','hyphen_url','underscore_url','slash_url','qm_url','eq_url','at_url','and_url','exclaim_url','space_url','tilde_url','comma_url','plus_url','astr_url','hash_url','dol_url','per_url','len_url','len_tld_url','http','https','port','query','dots_domain','hyphen_domain','underscore_domain','slash_domain','qm_domain','eq_domain','at_domain','and_domain','exclaim_domain','space_domain','tilde_domain','comma_domain','plus_domain','astr_domain','hash_domain','dol_domain','per_domain','len_domain','ip'
,'dots_path','hyphen_path','underscore_path','slash_path','qm_path','eq_path','at_path','and_path','exclaim_path','space_path','tilde_path','comma_path','plus_path','astr_path','hash_path','dol_path','per_path','len_path'
,'dots_par','hyphen_par','underscore_par','slash_par','qm_par','eq_par','at_par','and_par','exclaim_par','space_par','tilde_par','comma_par','plus_par','astr_par','hash_par','dol_par','per_par','len_par']

for x in urls:
    cur=[]
    cur.append(x.count('.'))
    cur.append(x.count('-'))
    cur.append(x.count('_'))
    cur.append(x.count('/'))
    cur.append(x.count('?'))
    cur.append(x.count('='))
    cur.append(x.count('@'))
    cur.append(x.count('&'))
    cur.append(x.count('!'))
    cur.append(x.count(' '))
    cur.append(x.count('~'))
    cur.append(x.count(','))
    cur.append(x.count('+'))
    cur.append(x.count('*'))
    cur.append(x.count('#'))
    cur.append(x.count('$'))
    cur.append(x.count('%'))
    cur.append(len(x))
    l=tldextract.extract(x)
    cur.append(len(l[2]))
    if (urlparse(x).scheme).lower()=='http':
        cur.append(1)
    else:
        cur.append(0)
    if (urlparse(x).scheme).lower()=='https':
        cur.append(1)
    else:
        cur.append(0)
    if urlparse(x).port:
        cur.append(1)
    else:
        cur.append(0)
    if urlparse(x).query:
        cur.append(1)
    else:
        cur.append(0)
    dom=urlparse(x).netloc
    cur.append(dom.count('.'))
    cur.append(dom.count('-'))
    cur.append(dom.count('_'))
    cur.append(dom.count('/'))
    cur.append(dom.count('?'))
    cur.append(dom.count('='))
    cur.append(dom.count('@'))
    cur.append(dom.count('&'))
    cur.append(dom.count('!'))
    cur.append(dom.count(' '))
    cur.append(dom.count('~'))
    cur.append(dom.count(','))
    cur.append(dom.count('+'))
    cur.append(dom.count('*'))
    cur.append(dom.count('#'))
    cur.append(dom.count('$'))
    cur.append(dom.count('%'))
    cur.append(len(dom))
    pattern=re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    res=pattern.match(dom)
    if res:
        cur.append(1)
    else:
        cur.append(0)
    p=urlparse(x).path
    cur.append(p.count('.'))
    cur.append(p.count('-'))
    cur.append(p.count('_'))
    cur.append(p.count('/'))
    cur.append(p.count('?'))
    cur.append(p.count('='))
    cur.append(p.count('@'))
    cur.append(p.count('&'))
    cur.append(p.count('!'))
    cur.append(p.count(' '))
    cur.append(p.count('~'))
    cur.append(p.count(','))
    cur.append(p.count('+'))
    cur.append(p.count('*'))
    cur.append(p.count('#'))
    cur.append(p.count('$'))
    cur.append(p.count('%'))
    cur.append(len(p))
    par=urlparse(x).params
    cur.append(par.count('.'))
    cur.append(par.count('-'))
    cur.append(par.count('_'))
    cur.append(par.count('/'))
    cur.append(par.count('?'))
    cur.append(par.count('='))
    cur.append(par.count('@'))
    cur.append(par.count('&'))
    cur.append(par.count('!'))
    cur.append(par.count(' '))
    cur.append(par.count('~'))
    cur.append(par.count(','))
    cur.append(par.count('+'))
    cur.append(par.count('*'))
    cur.append(par.count('#'))
    cur.append(par.count('$'))
    cur.append(par.count('%'))
    cur.append(len(par))
    df.append(cur)
datafr=pd.DataFrame(df,columns=col)
print(datafr.head)

features=datafr.iloc[:,:]

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(features,result,test_size=0.2,shuffle=True,random_state=1)

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion='entropy',random_state=0)
dtc.fit(xtrain,ytrain)

from sklearn.metrics import accuracy_score
ypred=dtc.predict(xtest)
score=accuracy_score(ytest,ypred)
print('dtc',score)

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=10,criterion='entropy')
rfc.fit(xtrain,ytrain)
ypred1=rfc.predict(xtest)
print('rfc',accuracy_score(ytest,ypred1))
import joblib

joblib.dump(dtc,'dtc.pkl')
